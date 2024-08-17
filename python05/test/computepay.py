def computepay(hours, rate):
        if  hours < 41 :
            pay = hours * rate
            return pay
        elif hours > 40 :
            pay = hours * rate + hours % 40 * rate * 0.5
            return pay

try:
    hours = float(input('How many hours do you work? \n'))
    rate = float(input('What is your hour rate? \n'))        
    x = computepay(hours, rate)
    print(x)
except:
    print('Please enter a number')