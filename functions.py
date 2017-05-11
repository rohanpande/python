#!/usr/bin/env python
def my_function():
    print("Hello from my function!")

my_function()

def my_function_with_args(username, greeting):
    print("Hello, %s, From My Function!, I wish you %s" %(username,greeting))

my_function_with_args('Rohan Pande', 'All the best')

def sum_two_numbers(a, b):
    return a + b

print sum_two_numbers(12, 12)
