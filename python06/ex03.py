""" Exercise 3: Encapsulate this code in a function named count, and generalize it
so that it accepts the string and the letter as arguments. 
 """

def count(string, a):
    cica = 0
    for letter in string:
        if letter == a :
            cica += 1
    return cica


user_input_string = input('Enter a word or sentence:\n')
user_input_letter = input('Which letter would you like to count?\n')
lemon = count(user_input_string, user_input_letter)
print(lemon)        
