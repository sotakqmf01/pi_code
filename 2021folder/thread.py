import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
red=23
yello=24
green=25
GPIO.setup(red,GPIO.OUT)
GPIO.setup(yello,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)

GPIO.output(red, GPIO.HIGH)
GPIO.output(yello, GPIO.HIGH)
GPIO.output(green, GPIO.HIGH)
print("turn-on")

time.sleep(10)
GPIO.cleanup()
print("cleanup")

