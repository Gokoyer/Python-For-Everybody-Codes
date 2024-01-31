"""
This is the first exercise in chapter 2 fof Python For Everybody
#.3 Write a program to prompt the user for hours and rate per hour
using input to compute gross pay. Use 35 hours and a rate of 2.75 per
hour to test the program (the pay should be 96.25). You should use input
to read a string and float() to convert the string to a number.
Do not worry about error checking or bad user data.
"""

x_hour = input("Enter Hours: ")
x_rate = input("Enter Rate: ")
x_p = float(x_hour) * float(x_rate)
print("pay:",x_p)