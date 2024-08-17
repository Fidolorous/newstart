# Multiple assignment with dictionaries
# Combining items, tuple assignment, and for, you can see a nice code pattern for
# traversing the keys and values of a dictionary in a single loop:

d = {'a':10, 'b':1, 'c':22}
for key, val in d.items():
    print(val, key)