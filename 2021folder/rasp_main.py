# 멀티 쓰레드 코드
import threading
import socket
import time
from imutils.video import VideoStream
import imagezmq
import RPi.GPIO as GPIO


# 라즈베리 파이에서 멀티 쓰레드를 사용하기.
# server 컴에서는 멀티 프로세스 사용하기.
# fork로 소켓 통신 프로그램을 라즈베리 쓰레드인 Tread2로 보내서 위험한 신호를 보내고.
# 라즈베리 파이에서 Tread2를 받았으면 해당 프로세스가 종료되게(자원을 회수되게) 한다.


class Tread1(threading.Thread):
    # 작업 1  : 이미지를 서버에 보내는 역할
    def run(self) -> None:
        # 라즈베리 파이 client 코드
        sender = imagezmq.ImageSender(connect_to='tcp://116.121.38.22:12222')
        
        rpi_name = socket.gethostname() # send RPi hostname with each image
        print("start", rpi_name)

        picam = VideoStream(usePiCamera=True).start()
        time.sleep(2.0)  # allow camera sensor to warm up
        print("..ing")
        while True:  # send images as stream until Ctrl-C
          image = picam.read()
          sender.send_image(rpi_name, image)
          
        
def lightling(value):
        
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    red=23
    yello=24
    green=25
    GPIO.setup(red,GPIO.OUT)
    GPIO.setup(yello,GPIO.OUT)
    GPIO.setup(green,GPIO.OUT)

    print("turn-on")
    if(value == 1):
        GPIO.output(green, GPIO.LOW)
        GPIO.output(yello, GPIO.LOW)
        GPIO.output(red, GPIO.HIGH)
        
    else:
        GPIO.output(red, GPIO.LOW)
        GPIO.output(yello, GPIO.LOW)
        GPIO.output(green, GPIO.HIGH)

class Tread2(threading.Thread):
    
        
    
    # 작업 2 : 위험한 신호가 1이면 신호등에 불을 키는 역할
    def run(self)-> None:
        # 라즈베리 파이 sever 코드 인데 신호등 코드까지 포함.
        # 접속할 서버 주소 지금은 로컬
        #host = '203.250.76.152'
        host = '192.168.0.118'
        # 클라이언트 접속을 대기하는 포트 번호
        port=30000
        #port =22
        time.sleep(5)
        print("start")
        # 소켓 생성
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 포트 사용중이라 연결할 수 없다는 WinError 10048 에러 해결을 위해 필요
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.listen()
        lightling(value=0)
        
        while True:
            
            client_socket, addr = server_socket.accept()
            print('접속 완료', addr)
            data = client_socket.recv(1024)
            if not data:
                break
            if data.decode() == '1':
                print("빨간불을 켜시오")
                lightling(value = 1)
                
            elif data.decode() == '0':
                print("파란불을 켜시오")
                lightling(value = 0)
            else:
                print("error ")
                print('Received from', addr, data.decode())
            client_socket.send(data)
            client_socket.close()
            
        server_socket.close()


t1 = Tread1()
t2 = Tread2()

t1.start()
# 하나 작업이 끝나면 동시에 종료 True
# 하나 작업이 끝나도 해당 작업만 종료하면 False
t2.start()
