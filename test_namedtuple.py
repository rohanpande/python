#!/usr/bin/env python3 

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(10, y =20)

print(p)

print (p.x + p.y)


