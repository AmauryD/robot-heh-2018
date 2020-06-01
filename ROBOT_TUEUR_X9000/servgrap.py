# Picon Zero Servo Test
# Use arrow keys to move 2 servos on outputs 0 and 1 for Pan and Tilt
# Use G and H to open and close the Gripper arm
# Press Ctrl-C to stop
#

import piconzero as pz
import time
from iniReader import IniReader


# ======================================================================
# Reading single character by forcing stdin to raw mode


# one static class by physical periph
class ServGrap:
    # static vars for easier code reading ...
    UP = 0
    DOWN = 1

    tiltVal = 90
    gripVal = 90
    panVal = 90

    @staticmethod
    def setup():
        print('initializing servGrap')

        # read channel from config
        channel = int(IniReader.read('pins', 'SERVO_CHANNEL'))

        # Set output mode to Servo
        pz.setOutputConfig(0, channel)
        pz.setOutputConfig(1, channel)
        pz.setOutputConfig(2, channel)

        print('resetting servo to DOWN position , waiting 1 second ...')
        ServGrap.hook(ServGrap.DOWN)
        time.sleep(1)
        print('servGrap initialised and ready')

    @staticmethod
    #rotate the servo by 90 degrees UP or DOWN
    def hook(side):
        if side == ServGrap.UP:
            ServGrap.panVal = min(180, ServGrap.panVal + 90)  # up
        elif side == ServGrap.DOWN:
            ServGrap.panVal = ServGrap.tiltVal = ServGrap.gripVal = 90  # down

        pz.setOutput(0, ServGrap.panVal)
        pz.setOutput(1, ServGrap.tiltVal)
        pz.setOutput(2, ServGrap.gripVal)
