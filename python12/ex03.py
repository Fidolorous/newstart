# Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving the document from a URL, 
# (2) displaying up to 3000 characters, and (3) counting the
# overall number of characters in the document. Don’t worry about the headers for
# this exercise, simply show the first 3000 characters of the document contents.

import urllib.request
count = 0

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo-full.txt')
for line in fhand:
    if count < 3001: 
        print(line.decode().strip())
    for character in line.decode():
            count += 1
print(count, 'characters')
