import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)  # BCM direct connect
GPIO.setwarnings(False)

T = 3
GPIO.setup(T,GPIO.OUT)
GPIO.output(T,GPIO.HIGH)
print("red")
time.sleep(5)
GPIO.output(T,GPIO.LOW)

GPIO.cleanup()
print("clean")
time.sleep(1)
