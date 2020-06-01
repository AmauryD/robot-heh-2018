# coding=utf-8
from movement import Movement
from ultrasonicSensor import UltrasonicSensor


class SpeedTest:
    @staticmethod
    def run():
        d1 = UltrasonicSensor.pulse()
        Movement.fw(duration=1)
        d2 = UltrasonicSensor.pulse()

        print('speed : ' + str(abs(d2 - d1)) + 'cm/s')
