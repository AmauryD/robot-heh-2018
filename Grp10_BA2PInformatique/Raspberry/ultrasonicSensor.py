import RPi.GPIO as GPIO, sys, threading, time, os, subprocess

from iniReader import IniReader


class UltrasonicSensor:
    @staticmethod
    def setup():
        print("Init GPIO Sensor module")
        GPIO.setmode(GPIO.BOARD)
        print("Init GPIO Sensor module done")

    @staticmethod
    def pulse():
        # get pin number
        sonar_pin = int(IniReader.read('pins', 'SONAR_PIN'))

        # Set pins as output and input
        GPIO.setup(sonar_pin, GPIO.OUT)
        # Send 10us pulse to trigger
        GPIO.output(sonar_pin, True)
        time.sleep(0.00001)
        GPIO.output(sonar_pin, False)
        start = time.time()
        count = time.time()
        GPIO.setup(sonar_pin, GPIO.IN)

        while GPIO.input(sonar_pin) == 0 and time.time() - count < 0.1:
            start = time.time()
        count = time.time()
        stop = count
        while GPIO.input(sonar_pin) == 1 and time.time() - count < 0.1:
            stop = time.time()

        # Calculate pulse length
        elapsed = stop - start
        # Distance pulse travelled in that time is time
        # multiplied by the speed of sound (cm/s)
        distance = elapsed * 34000
        # That was the distance there and back so halve the value
        distance = distance / 2
        return distance
