# coding=utf-8
import time

from application import Application as ap
from movement import Movement


# SUR BATTERIE
# pz.spinLeft(100)
# tourner droite time.sleep(1.05)
# tourner droite boite time.sleep(1.33)

# demi tour sans boite
# pz.spinLeft(100)
# time.sleep(1.05)
# pz.spinLeft(100)
# time.sleep(1.05)

# SUR SECTEUR
# AVEC BOITE
# demi-tour
# time.sleep(2.4)
#
# tourner à droite
# time.sleep(1.2)
#
# SANS BOITE
# demi-tour
# time.sleep(0.92 * 2)
#
# tourner à froite
# time.sleep(0.91)

# main function
from servgrap import ServGrap
from speedTest import SpeedTest


def main():
    # setup the static classes
    ap.init()

    #try to handle the Ctrl-C and then clean the app
    try:
        #ServGrap.hook(ServGrap.UP)
        #time.sleep(1)
        #ServGrap.hook(ServGrap.DOWN)
        #time.sleep(1)
        Movement.snake()
    except KeyboardInterrupt:
        print('Ctrl C')
    finally:
        ap.cleanup()


main()
