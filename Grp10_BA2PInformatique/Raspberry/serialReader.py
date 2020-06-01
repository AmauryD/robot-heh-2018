import serial

from iniReader import IniReader


class SerialReader:
    @staticmethod
    # check if RFID is in front of the bot , 2-3cm range
    def hasRFID():
        # read serial interface from config
        ser = serial.Serial(IniReader.read('pins', 'SERIAL_INTERFACE'), 9600)
        # throws ErrorValue error when serial is disconnected
        if int(ser.read()) == 1:
            return True
        else:
            return False
