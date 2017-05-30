#!/usr/bin/env python
basic_salary = 1500
bonus_rate = 200
commission_rate = 0.02
numberofcamera = int(input("Enter the inputs sold: "))
price = float(input("Enter the total prices: "))
bonus = (bonus_rate * numberofcamera)
commission = (commission_rate * numberofcamera * price)

print("Bonus = %6.2f" % bonus)
print("Commission = %6.2f" % commission)
print("Gross salary = %6.2f" % (basic_salary + bonus + commission))
