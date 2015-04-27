#!/usr/bin/python

"""
This is a script to check if a number is a prime.

This is part of the Codecademy Python course.

It's really just a scratchpad for testing purposes.

Created: 12/04/2015
Last Modified: 12/04/2015


THe text below was my attempt:
x = int(raw_input("Enter a number: ")
for n in range(2,x):
    	print "n = " + str(n)
	print "Dividing: " + str(x) + " / " + str(n)
	print "Int answer: " + str(x / n)
	print "Float answer: " + str(float(x) / float(n))
	print "Difference: " + str((float(x)/float(n)) - (x / n))
	print
	print


############################################

#Here is the answer that passed
"""

def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2,x-1):
            dec_num = float(x) / float(n)
            int_num = x / n
            if dec_num == float(int_num):
                return False
        else:
            return True
