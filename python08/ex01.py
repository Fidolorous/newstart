# Exercise 1: Write a function called chop that takes a list and modifies it, removing
# the first and last elements, and returns None. Then write a function called middle
# that takes a list and returns a new list that contains all but the first and last
# elements.

def chop(t):
    del t[-1] 
    del t[0]

letters = ['a', 'b', 'c']
chop(letters)
print(letters)
