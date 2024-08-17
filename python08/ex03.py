# Exercise 3: Rewrite the guardian code in the above example 
# without two if statements. Instead, use a compound logical
# expression using the or logical operator
# with a single if statement.

with open('mbox-short.txt', 'r+') as beniopen:
    for line in beniopen:
        words = line.split()
        # print('Debug:', words)
        if len(words) == 0 or words[0] != 'From' : 
            continue
        elif len(words) <= 2 : 
            break
        print(words[2])





