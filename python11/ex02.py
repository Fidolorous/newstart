# Exercise 2: Write a program to look for lines of the form:
# New Revision: 39772
# Extract the number from each of the lines using a regular expression
# and the findall() method. Compute the average of the numbers and
# print out the average as an integer.
# Enter file:mbox.txt
# 38549
# Enter file:mbox-short.txt
# 39756

import string
import re
numlist = list()
inp = input("Enter file:")

with open(inp, 'r') as fhand:
    file_name = fhand.name
    for line in fhand:
        line.rstrip()
        refind = re.findall('^New Revision: ([0-9]+)', line)
        if len(refind) > 0:
            listtostring = str(refind)
            cleanstring = listtostring.translate(str.maketrans("", "", string.punctuation))
            num = int(cleanstring)
            numlist.append(num)

average = sum(numlist) / len(numlist)
print(int(average))
