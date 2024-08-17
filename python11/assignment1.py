# Finding Numbers in a Haystack

# In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.

# Data Files
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
# Actual data: http://py4e-data.dr-chuck.net/regex_sum_1791040.txt (There are 76 values and the sum ends with 177)
# These links open in a new window. Make sure to save the file into the same folder as you will be writing your Python program. Note: Each student will have a distinct data file for the assignment - so only use your own data file for analysis.

import string
import re
numlist = list()
inp = input("Enter file:")
count = 0

with open(inp, 'r') as fhand:
    file_name = fhand.name
    for line in fhand:
        line.rstrip()
        refind = re.findall('[0-9]+', line)
        if len(refind) > 0:
            for values in refind:
                count += 1
                value = str(values)
                valuestr = value.translate(str.maketrans("", "", string.punctuation))
                num = int(valuestr)
                numlist.append(num)

print(sum(numlist))
print(count)
