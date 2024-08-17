# Exercise 2: This program counts the distribution of the hour of the day for each
# of the messages. You can pull the hour from the “From” line by finding the time
# string and then splitting that string into parts using the colon character. Once
# you have accumulated the counts for each hour, print out the counts, one per line,
# sorted by hour as shown below.
# python timeofday.py
# Enter a file name: mbox-short.txt
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1

counts = dict()

with open('mbox-short.txt', "r") as fhand:
    for lines in fhand:
        if not lines.startswith("From"): continue
        words = lines.split()
        if len(words) <= 2 or len(words) == 0: continue 
        time = words[5]
        hours = time.split(':')
        hour = hours[0]
        if hour not in counts:
            counts[hour] = 1
        else:
            counts[hour] += 1
            
lst = list()

for key, val in list(counts.items()):
    lst.append((key, val))

lst.sort(reverse=False)

for key, val in lst:
    print(key, val)