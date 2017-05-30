#!/usr/bin/env python3
class Student(object):
    def __init__(self, name):
        self.name = name


std = Student("Rohan Pande")

print(std.name)

std.name = "Manoj Khande"

print(std.name)

