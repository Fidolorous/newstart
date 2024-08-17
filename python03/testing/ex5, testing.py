inp = input('What is the current degree in Celsius? \n')
try:
    celsius = float(inp)
    fahrenheit = (celsius* 9/5) + 32
    print ('The degree in Fahrenheit is:', fahrenheit)
except:
    print('Please enter a number')  