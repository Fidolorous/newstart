try:
    hours = float(input('How many hours do you work? \n'))
    rate = float(input('What is your hour rate? \n'))
    if  hours < 41 :
        pay = hours * rate
        print ('Your payment:', pay)
    elif hours > 40 :
        pay = hours * rate + hours % 40 * rate * 0.5
        print ('Your payment:', pay)
except:
    print('Please enter a number')
