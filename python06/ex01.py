""" Exercise 1: Write a while loop that starts at the last character in the string and
works its way backwards to the first character in the string, printing each letter on
a separate line, except backwards. """

cica = 'macska'
index = 0
while index < len(cica):
    if index == -6:
        break
    letter = cica[index-1]
    print(letter)
    index -= 1