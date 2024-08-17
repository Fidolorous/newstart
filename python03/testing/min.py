def min(values):
    smallest = None
    for value in values: 
        if smallest is None or value < smallest :
            smallest = value  
    return smallest

itervar = (3, 41, 12, 9, 74, 15)
x = min(itervar)
print(x)


""" 
print('Before:', smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest :
        smallest = itervar
    print('Loop:', itervar, smallest)
print('Smallest:', smallest) """

