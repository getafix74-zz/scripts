#!/usr/bin/python

"""
Codecademy exercise: purify.py
"""
number_list = [1,2,1,2,1,3]

def purify(number_list):
	purified_list = []
	for each in number_list:
		if each % 2 == 0:
			purified_list.append(each)
	print purified_list



purify(number_list)
