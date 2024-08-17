# Write a program that reads the words in words.txt and stores them as keys in
# a dictionary. It doesn’t matter what the values are. Then you can use the in
# operator as a fast way to check whether a string is in the dictionary.

count = 0
dictionary = dict()
# dictlist = list()
with open('words.txt', 'r') as beniopen:
    for line in beniopen:
        words = line.split()
        for word in words:
            count += 1
            if word in dictionary:
                continue
            dictionary[word] = count  
        # print('Debug:', dictionary)

if 'Writing' in dictionary:
    print('True')
else:
    print('False')
            
