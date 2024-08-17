# Exercise 3: Write a program that reads a file and prints the letters in decreasing
# order of frequency.
# Your program should convert all the input to lower case and only count the letters
# a-z. Your program should not count spaces, digits, punctuation, or anything other
# than the letters a-z. Find text samples from several different languages and see
# how letter frequency varies between languages. Compare your results with the
# tables at https://wikipedia.org/wiki/Letter_frequencies

import string 

counts = dict()
with open('macskafej.txt', "r") as fhand:
    for line in fhand:
        line = line.rstrip()
        # First two parameters are empty strings
        line = line.translate(str.maketrans("", "", string.punctuation))
        line = line.translate(str.maketrans("", "", string.digits))
        line = line.lower()
        words = line.split()
        for word in words:
            for letter in word:
                if letter not in counts:
                    counts[letter] = 1
                else:
                    counts[letter] += 1

# Sort the dictionary by value
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))
    
lst.sort(reverse=True)

for key, val in lst:
    print(key, val)
