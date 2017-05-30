#!/usr/bin/env python3

fobj = open("sample.txt")
print(fobj.readline())

# to read all the lines in text using this 

print('')
print('')

fobj2 = open("sample.txt")
print(fobj2.readlines())

print("")
print("")


## using to loop 
fobj3 = open("sample.txt")
for x in fobj3:
    print(x, end=' ')

