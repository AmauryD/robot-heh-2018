# coding=utf-8
import time

import piconzero as pz
from lineSensor import LineSensor
from serialReader import SerialReader
from servgrap import ServGrap
from ultrasonicSensor import UltrasonicSensor as us


# TURN enum
# can also invert values
class Turn:
    LEFT = 0
    RIGHT = 1

    @staticmethod
    def inverse(val):
        if val == Turn.LEFT:
            return Turn.RIGHT
        else:
            return Turn.LEFT


# Movement class alias Main class
class Movement:
    # found the box | found the line
    hasbox = False
    foundLine = False  # would be cool to have a thread
    lastTurn = Turn.RIGHT  # this var is inverted at every changeColumn()

    @staticmethod
    # snake() AKA main()
    def snake():
        while not Movement.foundLine or not Movement.hasbox:
            Movement.fw()  # forward each time no matter what
            if us.pulse() < 15 and not Movement.hasbox:
                Movement.Boxcheck()
            elif us.pulse() < 20 and Movement.hasbox:
                Movement.changeColumn()

        # has the box , found the cross , ready to drop the box !
        Movement.fw(duration=0.25)
        print('je dépose la boite')
        ServGrap.hook(ServGrap.DOWN)
        time.sleep(2)

    @staticmethod
    def fw(direction=1, duration=0.1, speed=100):
        pz.setMotor(0, speed * -direction)
        pz.setMotor(1, speed * -direction)

        Movement.checkCross()

        time.sleep(duration)
        pz.stop()  # stop motors after each movement

    @staticmethod
    def checkCross():
        if not Movement.foundLine and Movement.hasbox:
            Movement.foundLine = LineSensor.isOnLine()

    @staticmethod
    # left | right
    def turn(turn):
        print('je tourne')

        if Movement.hasbox:
            if turn == Turn.LEFT:
                pz.spinLeft(100)
            else:
                pz.spinLeft(-100)
            time.sleep(1.2)
        else:
            if turn == Turn.LEFT:
                pz.spinLeft(100)
            else:
                pz.spinLeft(-100)
            time.sleep(0.94)
        pz.stop()  # stop motors after each movement

    @staticmethod
    # turn back
    def turnaround():
        print('demi-tour')
        pz.spinLeft(100)
        if Movement.hasbox:
            time.sleep(3)
        else:
            time.sleep(0.94 * 2)
        pz.stop()  # stop motors after each movement

    @staticmethod
    # a column change , for 'snake' style movement
    def changeColumn():
        print('changement de colonne')
        Movement.lastTurn = Turn.inverse(Movement.lastTurn)

        back_time = 0.3 if Movement.hasbox else 0.5  # Ternary operator

        Movement.fw(-1, duration=back_time)
        Movement.turn(Movement.lastTurn)
        Movement.fw(1, duration=0.5)

        if us.pulse() < 20:
            Movement.turnaround()
        else:
            Movement.turn(Movement.lastTurn)

    @staticmethod
    # action when the robot grab the box
    def grab():
        print('je grab la boite')
        Movement.fw(-1, 0.5)
        Movement.turnaround()
        Movement.fw(-1, 1.5, 50)
        ServGrap.hook(ServGrap.UP)
        Movement.hasbox = True
        Movement.turnaround()

    @staticmethod
    def Boxcheck():
        Movement.fw(1, 1)
        if SerialReader.hasRFID() and not Movement.hasbox:
            Movement.grab()
        else:
            Movement.changeColumn()
