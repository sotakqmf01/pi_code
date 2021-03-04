import socket

host = '192.168.0.118'
#host = '127.0.0.1'
#host = '203.250.76.152'
# 클라이언트 접속을 대기하는 포트 번호
#port = 80
port=30000 
print("start")
# 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 포트 사용중이라 연결할 수 없다는 WinError 10048 에러 해결을 위해 필요
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((host, port))
server_socket.listen()
client_socket, addr = server_socket.accept()
print('Connected by', addr)
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    if data.decode() == '1':
        print("빨간불을 켜시오")
    elif data.decode() == '0':
        print("파란불을 켜시오")
    else:
        print("error ")
        print('Received from', addr, data.decode())
    client_socket.send(data)

client_socket.close()
server_socket.close()
