""" Write another program that prompts for a list of numbers as above
and at the end prints out both the maximum and minimum of the numbers instead
of the average. """

largest = None
smallest = None
while True:
    user_input = input('Enter a number: ')
    if user_input == 'done':
        break
    try:
        number = int(user_input)
    except:
        print('Invalid input')
        continue
    if largest is None or number > largest :
        largest = number
    if smallest is None or number < smallest :
        smallest = number
        print(number)
print('Results are \n Max: ', largest, '\n Min: ', smallest)