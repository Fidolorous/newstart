import string

fname = input('Enter the file name: ')
counts = dict()
try:
    with open(fname, "r") as fhand:
        for line in fhand:
            line = line.rstrip()
            # First two parameters are empty strings
            line = line.translate(line.maketrans("", "", string.punctuation))
            line = line.lower()
            words = line.split()
            for word in words:
                if word not in counts:
                    counts[word] = 1
                else:
                    counts[word] += 1

except:
    print('File cannot be opened:', fname)
    exit()
print(counts)