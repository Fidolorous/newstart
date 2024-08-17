""" Exercise 5: Slicing strings
Take the following Python code that stores a string:
str = 'X-DSPAM-Confidence: 0.8475'
Use find and string slicing to extract the portion of the string after the colon
character and then use the float function to convert the extracted string into a
floating point number."""

str = 'X-DSPAM-Confidence: 0.8475'
atpos = str.find(':')
sppos = str.find('5',atpos)
host = float(str[atpos+2:sppos+1])
print(host)
tipe = type(host)
print(tipe)