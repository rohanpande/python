#!/usr/bin/env python3

from collections import defaultdict

s = [('Yellow', 1), ('blue', 2), ('Yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)

for k, v in s:
    d[k].append(v)

print(d.items())
