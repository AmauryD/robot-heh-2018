import RPi.GPIO as GPIO

import piconzero as pz
from lineSensor import LineSensor
from servgrap import ServGrap
from ultrasonicSensor import UltrasonicSensor


class Application:
    @staticmethod
    # initialize the static classes , 'piconzero' and 'GPIO'
    def init():
        print('=======   App init    =====')
        pz.init()
        GPIO.setwarnings(False)
        LineSensor.setup()
        ServGrap.setup()
        UltrasonicSensor.setup()
        print('=======App initialized=====')

    @staticmethod
    #call the cleanup functions
    def cleanup():
        pz.stop()
        pz.cleanup()
        GPIO.cleanup()
        print('=======App cleaned up======')
