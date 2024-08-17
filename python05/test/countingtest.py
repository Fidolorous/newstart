count = 0
total = 0
while True:
    user_input = input('Enter a number:')
    if user_input == 'done':
        break
    count = count + 1
    try:
        total = total + float(user_input)
        print(user_input)
    except:
        print('Invalid input')
        continue
print('Results are:', count, total, total / count)