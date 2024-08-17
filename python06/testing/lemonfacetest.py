""" Exercise 3: Encapsulate this code in a function named count, and generalize it
so that it accepts the string and the letter as arguments.  
 """

""" HOMEWORK 19/01/24: FIGURE OUT HOW TO TAKE ONLY STRING AS INPUT AND NOT NUMBERS """
def count(string, a):
    cica = 0
    for letter in string:
        if letter == a :
            cica = cica + 1
    return cica

try:
    user_input_string = str(input('Enter a word or sentence:\n'))
    user_input_letter = str(input('Which letter would you like to count?\n'))
    lemon = count(user_input_string, user_input_letter)
    print(lemon)        
except:
    print('enter a string bro')