#!/usr/bin/env python
#import foo.bar
from foo import bar
import re

list = dir(re)
findList = []

for word in list:
    if(word.startswith('find')):
        findList.append(word)

print(sorted(findList))




