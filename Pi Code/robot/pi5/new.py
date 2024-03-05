"""
Title: RoboClawLib
Author: Joseph Caligiuri
Description: This is an open source lib for using Roboclaw motor controllers with python. 
I made this one as the offical roboclaw one apears to be outdated and not working.
"""




import random 
import serial
import struct
import time

class Roboclaw:
    "Interface with Roboclaw"

    def __init__(self, comport, rate, timeout=0.01, retries=3):
        self.comport = comport
        self.rate = rate
        self.timeout = timeout
        self._trystimeout = retries
        self._crc = 0

    class Cmd():
        M1FORWARD = 0
        M1BACKWARD = 1
        SETMINMB = 2
        SETMAXMB = 3
        M2FORWARD = 4
        M2BACKWARD = 5
        M17BIT = 6
        M27BIT = 7
        MIXEDFORWARD = 8
        MIXEDBACKWARD = 9
        MIXEDRIGHT = 10
        MIXEDLEFT = 11
        MIXEDFB = 12
        MIXEDLR = 13
        GETM1ENC = 16
        GETM2ENC = 17
        GETM1SPEED = 18
        GETM2SPEED = 19
        RESETENC = 20
        GETVERSION = 21
        SETM1ENCCOUNT = 22
        SETM2ENCCOUNT = 23
        GETMBATT = 24
        GETLBATT = 25
        SETMINLB = 26
        SETMAXLB = 27
        SETM1PID = 28
        SETM2PID = 29
        GETM1ISPEED = 30
        GETM2ISPEED = 31
        M1DUTY = 32
        M2DUTY = 33
        MIXEDDUTY = 34
        M1SPEED = 35
        M2SPEED = 36
        MIXEDSPEED = 37
        M1SPEEDACCEL = 38
        M2SPEEDACCEL = 39
        MIXEDSPEEDACCEL = 40
        M1SPEEDDIST = 41
        M2SPEEDDIST = 42
        MIXEDSPEEDDIST = 43
        M1SPEEDACCELDIST = 44
        M2SPEEDACCELDIST = 45
        MIXEDSPEEDACCELDIST = 46
        GETBUFFERS = 47
        GETPWMS = 48
        GETCURRENTS = 49
        MIXEDSPEED2ACCEL = 50
        MIXEDSPEED2ACCELDIST = 51
        M1DUTYACCEL = 52
        M2DUTYACCEL = 53
        MIXEDDUTYACCEL = 54
        READM1PID = 55
        READM2PID = 56
        SETMAINVOLTAGES = 57
        SETLOGICVOLTAGES = 58
        GETMINMAXMAINVOLTAGES = 59
        GETMINMAXLOGICVOLTAGES = 60
        SETM1POSPID = 61
        SETM2POSPID = 62
        READM1POSPID = 63
        READM2POSPID = 64
        M1SPEEDACCELDECCELPOS = 65
        M2SPEEDACCELDECCELPOS = 66
        MIXEDSPEEDACCELDECCELPOS = 67
        SETM1DEFAULTACCEL = 68
        SETM2DEFAULTACCEL = 69
        SETPINFUNCTIONS = 74
        GETPINFUNCTIONS = 75
        SETDEADBAND = 76
        GETDEADBAND = 77
        RESTOREDEFAULTS = 80
        GETTEMP = 82
        GETTEMP2 = 83
        GETERROR = 90
        GETENCODERMODE = 91
        SETM1ENCODERMODE = 92
        SETM2ENCODERMODE = 93
        WRITENVM = 94
        READNVM = 95
        SETCONFIG = 98
        GETCONFIG = 99
        SETM1MAXCURRENT = 133
        SETM2MAXCURRENT = 134
        GETM1MAXCURRENT = 135
        GETM2MAXCURRENT = 136
        SETPWMMODE = 148
        GETPWMMODE = 149
        READEEPROM = 252
        WRITEEEPROM = 253
        FLAGBOOTLOADER = 255

    def crc_clear(self):
        self._crc = 0
        return
    
    def crc_update(self, data):
        self._crc = self._crc ^ (data << 8)
        for bit in range(0, 8):
            if (self._crc&0x8000) == 0x8000:
                self._crc = ((self._crc << 1)^ 0x1021)
            else:
                self._crc = self._crc << 1
        return
    
    def _sendcommand(self, address, command):
        self.crc_clear()
        self.crc_update(address)
        self._port.write(chr(address))
        self.crc_update(command)
        self._port.write(chr(command))
        return
    
    def _readchecksumword(self):
        data = self._port.read(2)

    def Open(self):
        try:
            self._port = serial.Serial(port=self.comport, baudrate=self.rate, timeout=1, interCharTimeout=self.timeout)
        except:
            return 0
        return 1