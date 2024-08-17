# this is a test file to get more into the string module and the stuff we can use from is

import string

with open ('macskafej.txt', 'r') as fhand:
    for line in fhand:
        print('Line before:', '\n', line)
        line = line.rstrip()
        print('Debug for rstrip:', '\n',line)
        line = line.translate(str.maketrans("", "", string.punctuation))
        line = line.translate(str.maketrans("", "", string.digits))
        string.
        print('Debug for translate:', '\n',line)
# print(string.punctuation, '\n', string.digits, '\n', string.whitespace)
