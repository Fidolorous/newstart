""" Exercise 2: Write a program to prompt for a file name, and then read through
the file and look for lines of the form:
X-DSPAM-Confidence: 0.8475
When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart
the line to extract the floating-point number on the line. Count these lines and
then compute the total of the spam confidence values from these lines. When you
reach the end of the file, print out the average spam confidence.
 """

count = 0
total = 0
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('X-DSPAM-Confidence: '):
        continue
    results = line[20:]
    floatresults = float(results)
    decimal_part_length = [floatresults]
    lendecimal = len(decimal_part_length)
    print(lendecimal)
"""     while True:
        for itervar in floatresults:
            count += 1
            print(count)
        if count != 0:
            break """