def min(values):
    smallest = None
    for value in values:
        if smallest is None or value < smallest:    
            smallest = value
    return smallest

x = input('Enter a number')
c = min(x)
print(c)
