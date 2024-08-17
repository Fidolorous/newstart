# Search for lines that contain 'From'

import re
count = 0
with open('mbox.txt', 'r') as fhand:
    for line in fhand:
        line.rstrip()
        if re.search('From:', line):
            count += 1
    print(count)