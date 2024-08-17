# Exercise 2: Change your socket program so that it counts the number of characters it has received and stops displaying any text after it has shown 3000 characters.
# The program should retrieve the entire document and count the total number of
# characters and display the count of the number of characters at the end of the document.

import socket
import re

size = 0
count = 0
wholedoc = []

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
        data = mysock.recv(500)
        if len(data) < 1: break #if there is no more data to read, break
        count = count + len(data)
        decoded = data.decode()
        wholedoc.append(decoded)
        if count < 3001: 
            print(data.decode(),end='')


    mysock.close()
    joined = ''.join(wholedoc)

    #this is for the search once we ready with the list
    pattern = r'\r\n\r\n'
    match = re.search(pattern, joined)
    if match:
        start_index = match.end()
        for character in joined[start_index:]:               
                size += 1        
    print('\n''The total number of characters are:', size)


except:
    print('Enter correct URL')

