#!/usr/bin/env python

count = 0
# break
while True:
    print(count)
    count += 1
    if count >= 5: 
        break

print ' '
print ' '
# continue
for x in range(10):
    if x % 2 == 0: 
        continue
    print(x)
