""" Write a program which repeatedly reads integers until the user enters
“done”. Once “done” is entered, print out the total, count, and average of the
integers. If the user enters anything other than a integers, detect their mistake
using try and except and print an error message and skip to the next integers.
 """
count = 0
total = 0
while True:
    user_input = input('Enter a number: ')
    if user_input == 'done':
        break
    try:
        number = int(user_input)
    except:
        print('Invalid input')
        continue
    count += 1
    total += number
    print(number)
if count != 0:
    print('Results are:', count, total, total / count)