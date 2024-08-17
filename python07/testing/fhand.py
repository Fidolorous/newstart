fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('error')
    exit()    
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count += 1
print('There were', count, 'subject lines in', fname)
