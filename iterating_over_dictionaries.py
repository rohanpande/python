#!/usr/bin/env python
contactbook = {
   "Rohan" : 9371457725,
   "Manoj" : 9422275760,
   "Gaurav" : 8624025975,
   "Jill" : 8149075760
 }

for name, number in contactbook.items():
     print("Phone number of %s is %d" % (name, number))

