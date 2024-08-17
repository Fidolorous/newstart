# Exercise 1: Change the socket program socket1.py to prompt the user for the
# URL so it can read any web page.
# You can use split('/') to break the URL into its component parts so you can
# extract the host name for the socket connect call. Add error checking using try
# and except to handle the condition where the user enters an improperly formatted
# or non-existent URL.

import socket

try:
    url = input('Enter - ')
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    urlsplit = url.split('/')
    hostname = urlsplit[2]
    mysock.connect((hostname, 80))
    get = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
    cmd = get.encode()
    print(cmd)
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')

    mysock.close()

except:
    print('Enter correct URL')