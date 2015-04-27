#! /usr/bin/python

"""
This is a script to calculate the factorial of a given number.

It's part of the Codecademy Python course.
Created: 12/04/2015
Last edited: 12/04/2015

notes: This is just a script to practice some of the functions
"""

total = 0
x = int(raw_input("Enter a number: "))
for each in range(1,x+1):
	print "Number: " + str(each)
	if each == 1:
		total += 1
		print "adding 1"
	else:
		print "Multiplying " + str(total) + " by " + str(each)
		total = total * each
	print "Total is now: " + str(total)
	print
	print
