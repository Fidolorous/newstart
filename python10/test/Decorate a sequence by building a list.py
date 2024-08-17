# Decorate a sequence by building a list of tuples with one or more sort keys
# preceding the elements from the sequence,
# Sort the list of tuples using the Python built-in sort, and
# Undecorate by extracting the sorted elements of the sequence.
# For example, suppose you have a list of words and you want to sort them from
# longest to shortest:

txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))

t.sort(reverse=True)

res = list()
for length, word in t:
    res.append(word)

print(res)