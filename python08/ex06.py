# Exercise 6:
# Rewrite the program that prompts the user for a list of numbers and prints out the
# maximum and minimum of the numbers at the end when the user enters “done”.
# Write the program to store the numbers the user enters in a list and use the max()
# and min() functions to compute the maximum and minimum numbers after the
# loop completes.

numberlist = list()
while True:
    user_input = input('Enter a number: ')
    if user_input == 'done': break
    try:
        number = user_input
    except:
        print('Invalid input')
        continue
    print(number)
    value = float(number)
    numberlist.append(value)
print('Maximum:',max(numberlist))
print('Minimum:',min(numberlist))