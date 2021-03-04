import socket
import time
from imutils.video import VideoStream
import imagezmq

# user_ip_desktop = 192.168.0.3

# user_IP

#sender = imagezmq.ImageSender(connect_to='tcp://192.168.0.13:5555')

#Sender = imagezmq.ImageSender(connect_to='tcp://192.168.0.170:5555')
sender = imagezmq.ImageSender(connect_to='tcp://116.121.38.22:12222')
#sender = imagezmq.ImageSender(connect_to='tcp://1.253.92.196:11222')

rpi_name = socket.gethostname() # send RPi hostname with each image
print("start", rpi_name)

picam = VideoStream(usePiCamera=True).start()
time.sleep(2.0)  # allow camera sensor to warm up
print("..ing")
while True:  # send images as stream until Ctrl-C
  image = picam.read()
  sender.send_image(rpi_name, image)
  
