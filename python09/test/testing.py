with open('mbox-short.txt', "r") as fhand:
    for lines in fhand:
        if not lines.startswith("From"): continue
        words = lines.split()
        lenwords = len(words)
        if len(words) <= 2 or len(words) == 0: continue 
        mail = words[1]
        domain = mail.split('@')
        print(domain[1])