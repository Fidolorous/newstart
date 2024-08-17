import string 

counts = dict()
with open('romeo-full.txt', "r") as fhand:
    for line in fhand:
        line = line.rstrip()
        # First two parameters are empty strings
        line = line.translate(str.maketrans("", "", string.punctuation))
        line = line.lower()
        words = line.split()
        for word in words:
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1

# Sort the dictionary by value
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:10]:
    print(key, val)

    