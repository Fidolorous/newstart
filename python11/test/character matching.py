# Search for lines that start with From and have an at sign

import re

with open('mbox-short.txt', 'r') as fhand:
    for line in fhand:
        line.rstrip
        if re.search('From: csev@', line):
            print(line)
            