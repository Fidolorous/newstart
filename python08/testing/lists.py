cheeses = ['Cheddar', 'Edam', 'Gouda']
numbers = [17, 23]
print('before: ', numbers)
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print('after: ', numbers)