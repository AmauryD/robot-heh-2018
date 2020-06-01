import piconzero as pz

from iniReader import IniReader


class LineSensor:
    channel = None  # static

    @staticmethod
    def setup():
        print("Init line sensor")
        # read from config file
        LineSensor.channel = int(IniReader.read('pins', 'LINE_SENSOR_CHANNEL'))
        pz.setInputConfig(LineSensor.channel, 0)  # set DIGITAL
        print("Line sensor initialised")

    @staticmethod
    def isOnLine():  # 0 on true
        if pz.readInput(LineSensor.channel) == 0:
            return True
        else:
            return False
