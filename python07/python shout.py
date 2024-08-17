""" Exercise 1: Write a program to read through a file and print the contents of the
file (line by line) all in upper case. """

fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('You fool')
    exit()   
inp = fhand.read()
capitalinp = inp.upper()
print(capitalinp[:255])


""" this is how I found the location:
findline = inp.find('-0500')
print(findline) """
    