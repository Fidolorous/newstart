#  (Advanced) Change the socket program so that it only shows data
# after the headers and a blank line have been received. Remember that recv receives
# characters (newlines and all), not lines.

import socket

url = 'http://data.pr4e.org/romeo-full.txt'
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
urlsplit = url.split('/')
hostname = urlsplit[2]
mysock.connect((hostname, 80))
get = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
cmd = get.encode()
mysock.send(cmd)
header = ''

# receive the header
while header.endswith('\r\n\r\n') is False:
    data = mysock.recv(512)
    decodeddata = data.decode()
    eol = decodeddata.find('\r\n\r\n')
    header = decodeddata[:eol+4]
if header.endswith('\r\n\r\n') is True:
    print(data[eol+4:].decode(),end='')
    while True:
        data = mysock.recv(512)
        if len(data) < 1: break #if there is no more data to read, break        
        print(data.decode(),end='')
mysock.close()