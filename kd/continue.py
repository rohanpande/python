#!/usr/bin/env python

while True:
    n = int(input("please enter an integer: "))
    if n < 0:
        continue
    elif n == 0:
        break
    print("Square is ", n ** 2)
print("Goodbye")

