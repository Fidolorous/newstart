# Because tuples are hashable and lists are not, if we want to create a composite key
# to use in a dictionary we must use a tuple as the key.
# We would encounter a composite key if we wanted to create a telephone directory
# that maps from last-name, first-name pairs to telephone numbers. Assuming that
# we have defined the variables last, first, and number, we could write a dictionary
# assignment statement as follows:

last = 'Swift'
first = 'Taylor'
directory = dict()
number = '+134570998'

directory[last,first] = number

for last, first in directory:
    print(first, last, directory[last,first])