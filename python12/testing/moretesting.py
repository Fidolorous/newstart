# The world’s simplest web browser
import socket
import string
import re

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = b'GET http://data.pr4e.org/romeo-full.txt HTTP/1.0\r\n\r\n'
print(cmd)
mysock.send(cmd)
wholedoc = []
size = 0

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    decoded = data.decode()
    wholedoc.append(decoded)
    
mysock.close()
joined = ''.join(wholedoc)

#this is for the search once we ready with the list
pattern = r'\r\n\r\n'
match = re.search(pattern, joined)
if match:
    start_index = match.end()
    for character in joined[start_index:]:
            size += 1        
print(joined)
print('The number of characters are:', size)