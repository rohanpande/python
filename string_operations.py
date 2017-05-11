#!/usr/bin/env python
astring = "Hello World!"
print("single quotes are ' '")
print(len(astring))

# this will give you the first position number of letter 'o' in a string
print(astring.index("o"))

# this will give you the number of times letter 'l' is present
print(astring.count("l"))

# tihs prints a slice of a string starting from index 3 and ending at index 6
print(astring[3:7])

# This prints the charachters of string from 3 to 7 skipping one character. This is extended slice syntax. The general form is [start:stop:step].

print(astring[3:7:2])

# This prints the characters of string from 3 to 7 skipping one character. This is extended slice syntax. The general form is [start:stop:step]. 
print(astring[3:7:1])

# you can reverse a string as follows 
print(astring[::-1])

# you can change the case of string as follows 
print(astring.upper())
print(astring.lower())

# This is used to determine whether the string starts with something or ends with something respectively 

print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

afewwords = astring.split(" ")

print(afewwords)
