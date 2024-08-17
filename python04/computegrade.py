def computegrade(score):
    if  score >= 0.9 :
        return('A')
    elif score >= 0.8 :
        return('B')
    elif score >= 0.7 :
        return('C')
    elif score >= 0.6 :
        return('D')
    elif score < 0.6 :
        return('F')
try:
    score = float(input('Enter score: \n'))
    x = computegrade(score)
    print(x)
except:
    print('Error: Enter score')
