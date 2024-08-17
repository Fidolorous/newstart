count = 0
sum = 0
input = input('Number')
for value in input:
    count = count + 1
    sum = sum + float(value)
print('Count: ', count, sum, sum / count)