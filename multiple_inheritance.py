#!/usr/bin/env python3

class Car(object):
    def __init__(self, speed, doors):
        self.speed = speed
        self.doors = doors


class Xylo(Car):
    def __init__(self, speed, doors):
        Car.__init__(self, speed, doors)
        self.speed = speed
        self.doors = doors

    def accerelate(self, count = 2):
        self.speed += count

class Innova(Car):
    def __init__(self, speed, doors):
        Car.__init__(self, speed, doors)
        self.speed = speed
        self.doors = doors

    def acceralate(self, count = 5):
        self.speed += count

