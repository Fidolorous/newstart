count = 0
sum = 0
while True:
    input = input('Number')
    for value in input:
        count = count + 1
        sum = sum + float(value)
    print(count, sum, sum / count)

    