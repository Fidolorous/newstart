# Exercise 1: Revise a previous program as follows: Read and parse the “From”
# lines and pull out the addresses from the line. Count the number of messages from
# each person using a dictionary.
# After all the data has been read, print the person with the most commits by
# creating a list of (count, email) tuples from the dictionary. Then sort the list in
# reverse order and print out the person who has the most commits.

counts = dict()

with open('mbox.txt', "r") as fhand:
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

lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:1]:
    print(val, key)            