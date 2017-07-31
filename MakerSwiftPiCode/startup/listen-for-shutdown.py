import RPi.GPIO as GPIO
import subprocess
import os

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN)
GPIO.wait_for_edge(3, GPIO.FALLING)
GPIO.cleanup()

os.system("sudo shutdown -h now")
