#!/usr/bin/env python
# coding: utf-8
#%%
"""
Simple client code for the ESP32 in Python - adapted from OFM Client
Copyright 2020 Richard Bowman, released under LGPL 3.0 or later
Copyright 2021 Benedict Diederich, released under LGPL 3.0 or later
"""
import json
import time
import numpy as np
import requests
import socket
from tempfile import NamedTemporaryFile
import serial
import serial.tools.list_ports

from .galvo import Galvo
from .config import config


try:
    import cv2
    is_cv2 = True
except:
    is_cv2 = False

try:
    from imswitch.imcommon.model import initLogger
    IS_IMSWITCH = True
except:
    print("No imswitch available")
    IS_IMSWITCH = False


    


class logger(object):
    def __init__(self):
        pass

    def error(self,message):
        print(message)

    def debug(self, message):
        print(message)
class ESP32Client(object):
    # headers = {'ESP32-version': '*'}
    headers={"Content-Type":"application/json"}
    getmessage = ""
    is_connected = False

    microsteppingfactor_filter=16 # run more smoothly
    filter_pos_1 = 1000*microsteppingfactor_filter # GFP
    filter_pos_2 = 0*microsteppingfactor_filter # AF647/SIR
    filter_pos_3 = 500*microsteppingfactor_filter
    filter_pos_LED = filter_pos_1 # GFP / Brightfield
    filter_pos_init = -1250*microsteppingfactor_filter
    filter_speed = microsteppingfactor_filter * 500
    filter_position_now = 0

    backlash_x = 0
    backlash_y = 0
    backlash_z = 0
    backlash_t = 0
    is_driving = False
    is_sending = False

    is_enabled = True

    is_wifi = False
    is_serial = False

    is_filter_init = False
    filter_position = 0

    steps_last_0 = 0
    steps_last_1 = 0
    steps_last_2 = 0
    steps_last_3 = 0

    BAUDRATE = 115200
    
    def __init__(self, host=None, port=31950, serialport=None, baudrate=BAUDRATE):
        '''
        This client connects to the UC2-REST microcontroller that can be found here
        https://github.com/openUC2/UC2-REST

        generally speaking you send/receive JSON documents that will cause an:
        1. action => "/XXX_act"
        2. getting => "/XXX_get"
        3. setting => "/XXX_set"

        you can send commands through wifi/http or usb/serial
        '''
        
        

        if IS_IMSWITCH:
            self.__logger = initLogger(self, tryInheritParent=True)
        else:
            self.__logger = logger()            

        # initialize galvos
        self.galvo1 = Galvo(channel=1)
        self.galvo2 = Galvo(channel=2)
        
        # initialize config
        self.config = config(self)

        self.serialport = serialport
        self.baudrate = baudrate


        # connect to wifi or usb
        if host is not None:
            # use client in wireless mode
            self.is_wifi = True
            self.host = host
            self.port = port

            # check if host is up
            self.is_connected = self.isConnected()
            if IS_IMSWITCH: self.__logger.debug(f"Connecting to microscope {self.host}:{self.port}")

        elif self.serialport is not None:
            self.initSerial(self.serialport,self.baudrate)

        else:
            self.is_connected = False
            if IS_IMSWITCH: self.__logger.error("No ESP32 device is connected - check IP or Serial port!")

        self.pinConfig = self.config.loadConfigDevice()
        self.__logger.debug("We are connected: "+str(self.is_connected))


    def initSerial(self,serialport,baudrate=None):
        # use client in wired mode
        self.serialport = serialport # e.g.'/dev/cu.SLAB_USBtoUART'
        self.is_serial = True
        
        if baudrate is None:
           baudrate = self.baudrate 

        if IS_IMSWITCH: self.__logger.debug(f'Searching for SERIAL devices...')
        self.is_connected = False
        try:
            self.serialdevice = serial.Serial(port=self.serialport, baudrate=baudrate, timeout=1)
            self.is_connected = True
            time.sleep(2) # let it warm up
        except:
            # try to find the PORT
            _available_ports = serial.tools.list_ports.comports(include_links=False)
            for iport in _available_ports:
                # list of possible serial ports
                if IS_IMSWITCH: self.__logger.debug(iport.device)
                portslist = ("COM", "/dev/tt", "/dev/a", "/dev/cu.SLA","/dev/cu.wchusb", "/dev/cu.usbserial") # TODO: Hardcoded :/
                descriptionlist = ("CH340")
                if iport.device.startswith(portslist) or iport.description.find(descriptionlist) != -1:
                    try:
                        self.serialdevice = serial.Serial(port=iport.device, baudrate=baudrate, timeout=1)
                        self.is_connected = True # attempting to initiliaze connection
                        time.sleep(2)
                        _state = self.get_state()
                        _identifier_name = _state["identifier_name"]
                        self.set_state(debug=False)
                        if _identifier_name == "UC2_Feather":
                            self.serialport = iport.device
                            self.__logger.debug("We are connected: "+str(self.is_connected) + " on port: "+iport.device)
                            return

                    except Exception as e:
                        if IS_IMSWITCH:
                            self.__logger.debug("Trying out port "+iport.device+" failed")
                            self.__logger.error(e)
                        self.is_connected = False


    def closeSerial(self):
        self.serialdevice.close()
        
    def isConnected(self):
        # check if client is connected to the same network
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.host, int(self.port)))
            s.settimeout(2)
            s.shutdown(2)
            return True
        except:
            return False

    @property
    def base_uri(self):
        return f"http://{self.host}:{self.port}"

    def get_json(self, path):
        """Perform an HTTP GET request and return the JSON response"""
        if self.is_connected and self.is_wifi:
            if not path.startswith("http"):
                path = self.base_uri + path
            try:
                r = requests.get(path)
                r.raise_for_status()
                self.is_connected = True

                self.getmessage = r.json()
                self.is_sending = False
                return self.getmessage

            except Exception as e:
                if IS_IMSWITCH: self.__logger.error(e)
                self.is_connected = False
                self.is_sending = False
                # not connected
                return None
        elif self.is_serial and self.is_connected:
            path = path.replace(self.base_uri,"")
            message = {"task":path}
            message = json.dumps(message)
            self.serialdevice.flushInput()
            self.serialdevice.flushOutput()
            returnmessage = self.serialdevice.write(message.encode(encoding='UTF-8'))
            return returnmessage
        else:
            return None

    def post_json(self, path, payload={}, headers=None, isInit=False, timeout=1):
        """Make an HTTP POST request and return the JSON response"""
        if self.is_connected and self.is_wifi:
            if not path.startswith("http"):
                path = self.base_uri + path
            if headers is None:
                headers = self.headers
            try:
                r = requests.post(path, json=payload, headers=headers,timeout=timeout)
                r.raise_for_status()
                r = r.json()
                self.is_connected = True
                self.is_sending = False
                return r
            except Exception as e:
                if IS_IMSWITCH: self.__logger.error(e)
                self.is_connected = False
                self.is_sending = False
                # not connected
                return None

        elif self.is_serial:
            try:
                payload["task"]
            except:
                payload["task"] = path
            try:
                is_blocking = payload['isblock']
            except:
                is_blocking = True
            self.writeSerial(payload)
            #self.__logger.debug(payload)
            returnmessage = self.readSerial(is_blocking=is_blocking, timeout=timeout)
            return returnmessage
        
    def writeSerial(self, payload):
        """Write JSON document to serial device"""
        try:
            self.serialdevice.flushInput()
            self.serialdevice.flushOutput()
        except Exception as e:
            self.__logger.error(e)
            try:
                del self.serialdevice
            except:
                pass
            self.is_connected=False
            # attempt to reconnect?
            try:
                self.initSerial(self.serialport, self.baudrate)
            except:
                return -1

        if type(payload)==dict:
            payload = json.dumps(payload)
        try:
            self.serialdevice.write(payload.encode(encoding='UTF-8'))
        except Exception as e:
            self.__logger.error(e)




    def readSerial(self, is_blocking=True, timeout = 15): # TODO: hardcoded timeout - not code
        """Receive and decode return message"""
        returnmessage = ''
        rmessage = ''
        _time0 = time.time()
        if is_blocking:
            while is_blocking:
                try:
                    rmessage =  self.serialdevice.readline().decode()
                    #self.__logger.debug(rmessage)
                    returnmessage += rmessage
                    if rmessage.find("--")==0:
                        break
                except:
                    pass
                if (time.time()-_time0)>timeout:
                    break
            # casting to dict
            try:
                returnmessage = json.loads(returnmessage.split("--")[0].split("++")[-1])
            except:
                self.__logger.debug("Casting json string from serial to Python dict failed")
                returnmessage = ""
        return returnmessage


    def loadConfig(self):
        return self.config.loadConfig()

    def setConfig(self,config={}):
        return self.config.setConfig(config)
            
    '''################################################################################################################################################
    HIGH-LEVEL Functions that rely on basic REST-API functions
    ################################################################################################################################################'''

    def move_x(self, steps=100, speed=1000, is_blocking=False, is_absolute=False, is_enabled=True):
        r = self.move_stepper(steps=(steps,0,0,0), speed=speed, timeout=1, backlash=(self.backlash_x,0,0,0), is_blocking=is_blocking, is_absolute=is_absolute, is_enabled=is_enabled)
        return r

    def move_y(self, steps=100, speed=1000, is_blocking=False, is_absolute=False, is_enabled=True):
        r = self.move_stepper(steps=(0,steps,0,0), speed=speed, timeout=1, backlash=(0,self.backlash_y,0,0), is_blocking=is_blocking, is_absolute=is_absolute, is_enabled=is_enabled)
        return r

    def move_z(self, steps=100, speed=1000, is_blocking=False, is_absolute=False, is_enabled=True):
        r = self.move_stepper(steps=(0,0,steps,0), speed=speed, timeout=1, backlash=(0,0,self.backlash_z,0), is_blocking=is_blocking, is_absolute=is_absolute, is_enabled=is_enabled)
        return r

    def move_xyz(self, steps=(0,0,0), speed=(1000,1000,1000), is_blocking=False, is_absolute=False, is_enabled=True):
        if len(speed)!= 3:
            speed = (speed,speed,speed)

        r = self.move_xyzt(steps=(steps[0],steps[1],steps[2],0), speed=(speed[0],speed[1],speed[2],0), is_blocking=is_blocking, is_absolute=is_absolute, is_enabled=is_enabled)
        return r

    def move_xyzt(self, steps=(0,0,0,0), speed=(1000,1000,1000,1000), is_blocking=False, is_absolute=False, is_enabled=True):
        if len(speed)!= 4:
            speed = (speed,speed,speed,speed)

        r = self.move_stepper(steps=steps, speed=speed, timeout=1, backlash=(self.backlash_x,self.backlash_y,self.backlash_z,self.backlash_t), is_blocking=is_blocking, is_absolute=is_absolute, is_enabled=is_enabled)
        return r

    def init_filter(self, nSteps, speed=250, filter_axis=-1, is_blocking = True, is_enabled=False):
        self.move_filter(steps=nSteps, speed=speed, filter_axis=filter_axis, is_blocking=is_blocking, is_enabled = is_enabled)
        self.is_filter_init = True
        self.filter_position_now = 0

    def switch_filter(self, filter_pos=0, filter_axis=-1, timeout=20, is_filter_init=None, speed=None, is_enabled=False, is_blocking=True):

        # switch off all lasers first!
        self.set_laser(1, 0)
        self.set_laser(2, 0)
        self.set_laser(3, 0)

        if speed is None:
            speed = self.filter_speed

        if is_filter_init is not None:
            self.is_filter_init = is_filter_init
        if not self.is_filter_init:
            self.init_filter(nSteps=self.filter_pos_init, speed=speed, filter_axis=filter_axis, is_blocking = True)

        # measured in steps from zero position
        steps = filter_pos - self.filter_position_now
        self.filter_position_now = filter_pos

        self.move_filter(steps=steps, speed=speed, filter_axis=filter_axis, is_blocking=is_blocking, timeout=timeout, is_enabled=is_enabled)


    def move_filter(self, steps=100, speed=200, filter_axis=-1, timeout=10, is_enabled=False, is_blocking=False):
        steps_xyzt = np.zeros(4)
        steps_xyzt[filter_axis] = steps
        r = self.move_stepper(steps=steps_xyzt, speed=speed, timeout=timeout, is_enabled=is_enabled, is_blocking=is_blocking)
        return r



    '''
    LOW-LEVEL FUNCTIONS

    These functions directly relate to the REST-API
    '''

    '''
    ##############################################################################################################################
    SLM
    ##############################################################################################################################
    '''
    def send_SLM_circle(self, posX, posY, radius, color, timeout=1):
        '''
        Send an LED array pattern e.g. an RGB Matrix: led_pattern=np.zeros((3,8,8))
        '''
        path = '/slm_act'
        payload = {
            "posX": posX,
            "posY": posY,
            "radius": radius,
            "color": color,
            "slmMode": "circle"
        }
        r = self.post_json(path, payload, timeout=timeout)
        return r

    def send_SLM_clear(self, timeout=1):
        '''
        Send an LED array pattern e.g. an RGB Matrix: led_pattern=np.zeros((3,8,8))
        '''
        path = '/slm_act'
        payload = {
            "slmMode": "clear"
        }
        r = self.post_json(path, payload, timeout=timeout)
        return r

    def send_SLM_full(self, color, timeout=1):
        '''
        Send an LED array pattern e.g. an RGB Matrix: led_pattern=np.zeros((3,8,8))
        '''
        path = '/slm_act'
        payload = {
            "color":color,
            "slmMode": "full"
        }
        r = self.post_json(path, payload, timeout=timeout)
        return r


    def send_SLM_image(self, image, startX, startY, timeout=1):
        '''
        Send an LED array pattern e.g. an RGB Matrix: led_pattern=np.zeros((3,8,8))
        '''
        path = '/slm_act'

        endX = startX+image.shape[0]
        endY = startY+image.shape[1]

        payload = {
            "color": image[:].flatten().tolist(),
            "startX":startX,
            "startY":startY,
            "endX":endX,
            "endY":endY,
            "slmMode": "image"
        }
        r = self.post_json(path, payload, timeout=timeout)
        return r


    '''
    ##############################################################################################################################
    LED ARRAY
    ##############################################################################################################################
    '''
    def send_LEDMatrix_array(self, led_pattern, timeout=1):
        '''
        Send an LED array pattern e.g. an RGB Matrix: led_pattern=np.zeros((3,8,8))
        '''
        path = '/ledarr_act'
        # Make sure LED strip is filled with matrix information
        if len(led_pattern.shape)<3:
            led_pattern = np.reshape(led_pattern, (led_pattern.shape[0], int(np.sqrt(led_pattern.shape[1])), int(np.sqrt(led_pattern.shape[1]))))
        led_pattern[:,1::2, :] = led_pattern[:,1::2, ::-1]
        payload = {
            "red": led_pattern[0,:].flatten().tolist(),
            "green": led_pattern[1,:].flatten().tolist(),
            "blue": led_pattern[2,:].flatten().tolist(),
            "arraySize": led_pattern.shape[1],
            "LEDArrMode": "array"
        }
        r = self.post_json(path, payload, timeout=timeout)
        return r

    def send_LEDMatrix_full(self, intensity = (255,255,255),timeout=1):
        '''
        set all LEDs with te same RGB value: intensity=(255,255,255)
        '''
        path = '/ledarr_act'
        payload = {
            "task":path,
            "red": int(intensity[0]),
            "green": int(intensity[1]),
            "blue": int(intensity[2]),
            "LEDArrMode": "full"
        }
        self.__logger.debug("Setting LED Pattern (full): "+ str(intensity))
        r = self.post_json(path, payload, timeout=timeout)
        return r

    def send_LEDMatrix_special(self, pattern="left", intensity = (255,255,255),timeout=1):
        '''
        set all LEDs inside a certain pattern (e.g. left half) with the same RGB value: intensity=(255,255,255), rest 0
        '''
        path = '/ledarr_act'
        payload = {
            "red": int(intensity[0]),
            "green": int(intensity[1]),
            "blue": int(intensity[2]),
            "LEDArrMode": pattern
        }
        self.__logger.debug("Setting LED Pattern (full): "+ str(intensity))
        r = self.post_json(path, payload, timeout=timeout)
        return r

    def send_LEDMatrix_single(self, indexled=0, intensity=(255,255,255), timeout=1):
        '''
        update only a single LED with a colour:  indexled=0, intensity=(255,255,255)
        '''
        path = '/ledarr_act'
        payload = {
            "red": int(intensity[0]),
            "green": int(intensity[1]),
            "blue": int(intensity[2]),
            "indexled": int(indexled),
            "LEDArrMode": "single"
        }
        self.__logger.debug("Setting LED PAttern: "+str(indexled)+" - "+str(intensity))
        r = self.post_json(path, payload, timeout=timeout)
        return r

    def send_LEDMatrix_multi(self, indexled=(0), intensity=((255,255,255)), timeout=1):
        '''
        update a list of individual LEDs with a colour:  led_pattern=(1,2,6,11), intensity=((255,255,255),(125,122,1), ..)
        '''
        path = '/ledarr_act'
        payload = {
            "red": intensity[0],
            "green": intensity[1],
            "blue": intensity[2],
            "indexled": indexled,
            "LEDArrMode": "multi"
        }
        self.__logger.debug("Setting LED PAttern: "+str(indexled)+" - "+str(intensity))
        r = self.post_json(path, payload, timeout=timeout)


    def get_LEDMatrix(self, timeout=1):
        '''
        get information about pinnumber and number of leds
        '''
        # TOOD: Not implemented yet
        path = "/ledarr_get"
        payload = {
            "task":path
        }
        r = self.post_json(path, payload, timeout=timeout)
        return r



    '''
    ##############################################################################################################################
    STATE
    ##############################################################################################################################
    '''
    def isControllerMode(self, timeout=1):
        # returns True if PS controller is active
        path = "/state_get"
        payload = {
            "task":path,
            "pscontroller": 1
        }
        r = self.post_json(path, payload, timeout=timeout)
        try:
            return r["pscontroller"]
        except:
            return False

    def espRestart(self,timeout=1):
        # if isController =True=> only PS jjoystick will be accepted
        path = "/state_act"
        payload = {
            "restart":1
            }
        r = self.post_json(path, payload, timeout=timeout)
        return r

    def setControllerMode(self, isController=False, timeout=1):
        # if isController =True=> only PS jjoystick will be accepted
        path = "/state_act"
        payload = {
            "task":path,
            "pscontroller": isController
        }
        r = self.post_json(path, payload, timeout=timeout)
        return r

    def isBusy(self, timeout=1):
        path = "/state_get"
        payload = {
            "task":path,
            "isBusy": 1
        }
        r = self.post_json(path, payload, timeout=timeout)
        try:
            return r["isBusy"]
        except:
            return r
    '''
    ##############################################################################################################################
    MOTOR
    ##############################################################################################################################
    '''
    def move_forever(self, speed=(0,0,0), is_stop=False, timeout=1):
        path = "/motor_act"
        payload = {
            "task":path,
            "speed0": np.int(speed[0]), # TODO: need a fourth axis?
            "speed1": np.int(speed[0]),
            "speed2": np.int(speed[1]),
            "speed3": np.int(speed[2]),
            "isforever":1,
            "isaccel":1,
            "isstop": np.int(is_stop)
        }
        # Make sure PS controller is treated correclty
        #if self.isControllerMode():
        #    self.setControllerMode(isController=False)
        #    PSwasActive = True
        #else:
        #    PSwasActive = False

        r = self.post_json(path, payload, timeout=0)

        #if PSwasActive:
        #    self.setControllerMode(isController=True)

        return r

    def move_stepper(self, steps=(0,0,0,0), speed=(1000,1000,1000,1000), is_absolute=False, timeout=1, backlash=(0,0,0,0), is_blocking=True, is_enabled=True):
        '''
        This tells the motor to run at a given speed for a specific number of steps; Multiple motors can run simultaneously
        '''
        if type(speed)!=list and type(speed)!=tuple  :
            speed = (speed,speed,speed,speed)

        path = "/motor_act"

        # detect change in directiongit config --global user.name "Your Name"
        if np.sign(self.steps_last_0) != np.sign(steps[0]):
            # we want to overshoot a bit
            steps_0 = steps[0] + (np.sign(steps[0])*backlash[0])
        else: steps_0 = steps[0]
        if np.sign(self.steps_last_1) != np.sign(steps[1]):
            # we want to overshoot a bit
            steps_1 =  steps[1] + (np.sign(steps[1])*backlash[1])
        else: steps_1 = steps[1]
        if np.sign(self.steps_last_2) != np.sign(steps[2]):
            # we want to overshoot a bit
            steps_2 =  steps[2] + (np.sign(steps[2])*backlash[2])
        else: steps_2 = steps[2]
        if np.sign(self.steps_last_3) != np.sign(steps[3]):
            # we want to overshoot a bit
            steps_3 =  steps[3] + (np.sign(steps[3])*backlash[3])
        else: steps_3 = steps[3]

        payload = {
            "task":"/motor_act",
            "pos0": np.int(steps_3),
            "pos1": np.int(steps_0),
            "pos2": np.int(steps_1),
            "pos3": np.int(steps_2),
            "isblock": int(is_blocking),
            "isabs": int(is_absolute),
            "speed0": np.int(speed[3]),
            "speed1": np.int(speed[0]),
            "speed2": np.int(speed[1]),
            "speed3": np.int(speed[2]),
            "isen": np.int(is_enabled)
        }
        self.steps_last_0 = steps_0
        self.steps_last_1 = steps_1
        self.steps_last_2 = steps_2
        self.steps_last_3 = steps_3

        # drive motor
        r = self.post_json(path, payload, timeout=timeout)

        #if PSwasActive:
        #    self.setControllerMode(isController=True)
        # wait until job has been done
        time0=time.time()
        if is_blocking:
            while self.isBusy():
                time.sleep(0.1)
                if time.time()-time0>timeout:
                    break

        return r


    def set_motor_maxSpeed(self, axis=0, maxSpeed=10000):
        path = "/motor_set",
        payload = {
            "task": path,
            "axis": axis,
            "maxspeed": maxSpeed
        }
        r = self.post_json(path, payload)
        return r

    def set_motor_currentPosition(self, axis=0, currentPosition=10000):
        path = "/motor_set",
        payload = {
            "task": path,
            "axis": axis,
            "currentposition": currentPosition
        }
        r = self.post_json(path, payload)
        return r

    def set_motor_acceleration(self, axis=0, acceleration=10000):
        path = "/motor_set",
        payload = {
            "task": path,
            "axis": axis,
            "acceleration": acceleration
        }
        r = self.post_json(path, payload)
        return r

    def set_motor_pinconfig(self, axis=0, pinstep=0, pindir=0):
        path = "/motor_set",
        payload = {
            "task": path,
            "axis": axis,
            "pinstep": pinstep,
            "pindir": pindir
        }
        r = self.post_json(path, payload)
        return r

    def set_motor_enable(self, is_enable=1):
        path = "/motor_set",
        payload = {
            "task": path,
            "isen": is_enable
        }
        r = self.post_json(path, payload)
        return r

    def set_motor_enable(self, axis=0, sign=1):
        path = "/motor_set",
        payload = {
            "task": path,
            "axis": axis,
            "sign": sign
        }
        r = self.post_json(path, payload)
        return r

    def set_direction(self, axis=1, sign=1, timeout=1):
        path = "/motor_set"

        payload = {
            "task":path,
            "axis": axis,
            "sign": sign
        }

        r = self.post_json(path, payload, timeout=timeout)
        return r

    def get_position(self, axis=1, timeout=1):
        path = "/motor_get"

        payload = {
            "task":path,
            "axis": axis
        }
        r = self.post_json(path, payload, timeout=timeout)
        _position = r["position"]
        return _position

    def set_position(self, axis=1, position=0, timeout=1):
        path = "/motor_set"
        if axis=="X": axis=1
        if axis=="Y": axis=2
        if axis=="Z": axis=3

        payload = {
            "task":path,
            "axis":axis,
            "currentposition": position
        }
        r = self.post_json(path, payload, timeout=timeout)

        return r



    '''
    ##############################################################################################################################
    Sensors
    ##############################################################################################################################
    '''
    def read_sensor(self, sensorID=0, NAvg=100):
        path = "/readsensor_act"
        payload = {
            "readsensorID": sensorID,
            "N_sensor_avg": NAvg,
        }
        r = self.post_json(path, payload)
        try:
            sensorValue = r['sensorValue']
        except:
            sensorValue = None
        return sensorValue
    # TODO: Get/SET methods missing
    '''
    ##############################################################################################################################
    PID controllers
    ##############################################################################################################################
    '''
    def set_pidcontroller(self, PIDactive=1, Kp=100, Ki=10, Kd=1, target=500, PID_updaterate=200):
        #{"task": "/PID_act", "PIDactive":1, "Kp":100, "Ki":10, "Kd":1, "target": 500, "PID_updaterate":200}
        #TOOD: PUt this into a class structure
        path = "/PID_act"
        payload = {
            "task": path,
            "PIDactive": PIDactive,
            "Kp": Kp,
            "Ki": Ki,
            "Kd": Kd,
            "target": target,
            "PID_updaterate": PID_updaterate
            }
        r = self.post_json(path, payload)
        return r

    '''
    ##############################################################################################################################
    LEDs
    ##############################################################################################################################
    '''
    def set_led(self, colour=(0,0,0)):
        payload = {
            "red": colour[0],
            "green": colour[1],
            "blue": colour[2]
        }
        path = '/led'
        r = self.post_json(path, payload)
        return r

    '''
    ##############################################################################################################################
    SCANNER
    ##############################################################################################################################
    '''
    def set_scanner_pattern(self, numpyPattern, scannernFrames=1,
            scannerLaserVal=32000,
            scannerExposure=500, scannerDelay=500, is_blocking = False):

        scannerMode="pattern"
        path = '/scanner_act'
        arraySize = int(np.prod(numpyPattern.shape))
        payload = {
            "task":path,
            "scannernFrames":scannernFrames,
            "scannerMode":scannerMode,
            "arraySize":arraySize,
            "i":numpyPattern.flatten().tolist(),
            "scannerLaserVal":scannerLaserVal,
            "scannerExposure":scannerExposure,
            "scannerDelay":scannerDelay,
            "isblock": is_blocking
            }

        r = self.post_json(path, payload)
        return r

    def set_scanner_classic(self, scannernFrames=100,
            scannerXFrameMin=0, scannerXFrameMax=255,
            scannerYFrameMin=0, scannerYFrameMax=255,
            scannerEnable=0, scannerxMin=1,
            scannerxMax=5, scanneryMin=1,
            scanneryMax=5, scannerXStep=25,
            scannerYStep=25, scannerLaserVal=32000,
            scannerExposure=500, scannerDelay=500):

        scannerModec="classic",
        path = '/scanner_act'
        payload = {
            "task":path,
            "scannernFrames":scannernFrames,
            "scannerMode":scannerModec,
            "scannerXFrameMin":scannerXFrameMin,
            "scannerXFrameMax":scannerXFrameMax,
            "scannerYFrameMin":scannerYFrameMin,
            "scannerYFrameMax":scannerYFrameMax,
            "scannerEnable":scannerEnable,
            "scannerxMin":scannerxMin,
            "scannerxMax":scannerxMax,
            "scanneryMin":scanneryMin,
            "scanneryMax":scanneryMax,
            "scannerXStep":scannerXStep,
            "scannerYStep":scannerYStep,
            "scannerLaserVal":scannerLaserVal,
            "scannerExposure":scannerExposure,
            "scannerDelay":scannerDelay}

        r = self.post_json(path, payload)
        return r


    def set_galvo_freq(self, axis=1, value=1000):
        if axis+1 == 1:
            self.galvo1.frequency=value
            payload = self.galvo1.return_dict()
        else:
            self.galvo2.frequency=value
            payload = self.galvo2.return_dict()

        r = self.post_json(payload["task"], payload, timeout=1)
        return r

    def set_galvo_amp(self, axis=1, value=1000):
        if axis+1 == 1:
            self.galvo1.amplitude=value
            payload = self.galvo1.return_dict()
        else:
            self.galvo2.amplitude=value
            payload = self.galvo2.return_dict()

        r = self.post_json(payload["task"], payload, timeout=1)
        return r

    def get_state(self, timeout=10):
        path = "/state_get"

        payload = {
            "task":path
        }
        r = self.post_json(path, payload, isInit=True, timeout=timeout)
        return r

    def set_state(self, debug=False, timeout=1):
        path = "/state_set"

        payload = {
            "task":path,
            "isdebug":int(debug)
        }
        r = self.post_json(path, payload, timeout=timeout)
        return r


    def set_laser(self, channel=1, value=0, auto_filterswitch=False,
                        filter_axis=-1, filter_position = None,
                        despeckleAmplitude = 0.,
                        despecklePeriod=10, timeout=20, is_blocking = True):
        if channel not in (0,1,2,3):
            if channel=="R":
                channel = 1
            elif channel=="G":
                channel = 2
            elif channel=="B":
                channel = 3

        if auto_filterswitch and value >0:
            if filter_position is None:
                if channel==1:
                    filter_position_toGo = self.filter_pos_1
                if channel==2:
                    filter_position_toGo = self.filter_pos_2
                if channel==3:
                    filter_position_toGo = self.filter_pos_3
                if channel=="LED":
                    filter_position_toGo = self.filter_pos_LED
            else:
                filter_position_toGo = filter_position

            self.switch_filter(filter_pos=filter_position_toGo, filter_axis=filter_axis, timeout=timeout,is_blocking=is_blocking)

        path = '/laser_act'

        payload = {
            "task": path,
            "LASERid": channel,
            "LASERval": value,
            "LASERdespeckle": int(value*despeckleAmplitude),
            "LASERdespecklePeriod": int(despecklePeriod),

        }

        r = self.post_json(path, payload)
        return r

    def sendTrigger(self, triggerId=0):
        path = '/digital_act'

        payload = {
            "task": path,
            "digitalid": triggerId,
            "digitalval": -1,
        }

        r = self.post_json(path, payload)
        return r



    def send_jpeg(self, image):
        if is_cv2:
            temp = NamedTemporaryFile()

            #add JPEG format to the NamedTemporaryFile
            iName = "".join([str(temp.name),".jpg"])

            #save the numpy array image onto the NamedTemporaryFile
            cv2.imwrite(iName,image)
            _, img_encoded = cv2.imencode('test.jpg', image)

            content_type = 'image/jpeg'
            headers = {'content-type': content_type}
            payload = img_encoded.tostring()
            path = '/uploadimage'

            #r = self.post_json(path, payload=payload, headers = headers)
            #requests.post(self.base_uri + path, data=img_encoded.tostring(), headers=headers)
            files = {'media': open(iName, 'rb')}
            if self.is_connected:
                requests.post(self.base_uri + path, files=files)



#if __name__ == '__main__':
    
