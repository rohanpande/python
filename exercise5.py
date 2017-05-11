#!/usr/bin/env python

s = "Hey there! what should this string be?"

# Length should be 20
print("Length of s = %d" % len(s))

# First occurance of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index('a'))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits 
print("The first five characters are '%s'" % s[:5])

# Start to 5 
print("The next five characters are '%s'" % s[5:10])

# Just number 12
print("The thirteenth character is '%s'" % s[12])

#(0-based indexing)
print("The characters with odd index are '%s'" % s[1::2])

# 5th-from-last to end
print("The last 5 characters are '%s'" % s[-5:])

# convert everything to uppper case
print("String in upper case: %s" % s.upper())

# convert everythingto lower case
print("String in lower case: %s" % s.lower())

# Check how a string starts 
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends 
if s.endswith('ome!'):
    print("String ends with 'ome!'. Good!")

print("Split the words of the string: %s" % s.split(" "))


