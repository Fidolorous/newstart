""" The following program counts the number of times the letter “a” appears in a
string: """

word = 'aaaaa'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)