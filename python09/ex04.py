# Exercise 4: Add code to the above program to figure out who has the most
# messages in the file. After all the data has been read and the dictionary has
# been created, look through the dictionary using a maximum loop (see Chapter 5:
# Maximum and minimum loops) to find who has the most messages and print how
# many messages the person has.
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
# Enter a file name: mbox.txt
# zqian@umich.edu 195

fname = input('Enter the file name: ')
counts = dict()
try:
    with open(fname, "r") as fhand:
        for lines in fhand:
            if not lines.startswith("From"): continue
            words = lines.split()
            lenwords = len(words)
            if len(words) <= 2 or len(words) == 0: continue 
            mail = words[1]
            if mail not in counts:
                counts[mail] = 1
            else:
                counts[mail] += 1
except:
    exit
lst = list(counts.keys())
largest = None
for key in counts:
    if largest is None or counts[key] > largest :
        largest = counts[key]
for mail in lst:
    if largest == counts[mail]:
        print(mail, counts[mail])