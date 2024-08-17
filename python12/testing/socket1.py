# The world’s simplest web browser
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.dr-chuck.com', 80))
cmd = b'GET /page1.htm HTTP/1.0\r\nHost: www.dr-chuck.com\r\n\r\n'
print(cmd)
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()