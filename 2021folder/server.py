import cv
import imagezmq

image_hub = imagezmq.ImageHub()
print("server start")

while True:
  rpi_name, image = image_hub.recv_image()
  cv2.imshow(rpi_name, image)
  if cv2.waitKey(1) == ord('q'):
    break
  
  image_hub.send_reply(b'OK')
