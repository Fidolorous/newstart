# Exercise 5: This program records the domain name (instead of the address) where
# the message was sent from instead of who the mail came from (i.e., the whole email
# address). At the end of the program, print out the contents of your dictionary.
# python schoolcount.py
# Enter a file name: mbox-short.txt
# {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
# 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

counts = dict()
with open('mbox-short.txt', "r") as fhand:
    for lines in fhand:
        if not lines.startswith("From"): continue
        words = lines.split()
        lenwords = len(words)
        if len(words) <= 2 or len(words) == 0: continue 
        mail = words[1]
        mails = mail.split('@')
        domain = mails[1]
        if domain not in counts:
            counts[domain] = 1
        else:
            counts[domain] += 1
    print(counts)