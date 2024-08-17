# Search for lines that contain 'From'
import re
with open('mbox-short.txt', 'r') as fhand:
    for line in fhand:
        line.rstrip()
        if re.search('From:', line):
            print(line)
