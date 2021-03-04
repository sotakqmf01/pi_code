import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)  # BCM direct connect
GPIO.setwarnings(False)

red = 23
yello = 24
green = 25
T = 3

GPIO.setup(red,GPIO.OUT)
GPIO.setup(yello,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)

GPIO.setup(T,GPIO.OUT)

for i in range(1,5):
    GPIO.output(T,True)
    GPIO.output(red,GPIO.HIGH)
    print("red")
    time.sleep(5)
    
    GPIO.output(T,False)
    GPIO.output(red,GPIO.LOW)
    GPIO.output(yello,GPIO.LOW)
    GPIO.output(green,GPIO.LOW)
    
    GPIO.output(T,True)
    GPIO.output(yello,GPIO.HIGH)
    print("yello")
    time.sleep(5)

    GPIO.output(T,False)
    GPIO.output(red,GPIO.LOW)
    GPIO.output(yello,GPIO.LOW)
    GPIO.output(green,GPIO.LOW)

    GPIO.output(T,True)
    GPIO.output(green,GPIO.HIGH)
    print("green")
    time.sleep(5)
    
    GPIO.output(T,False)
    GPIO.output(red,GPIO.LOW)
    GPIO.output(yello,GPIO.LOW)
    GPIO.output(green,GPIO.LOW)
    
GPIO.cleanup()
print("clean")
time.sleep(1)