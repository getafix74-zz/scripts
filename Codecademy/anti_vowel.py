#!/usr/bin/python

"""
This is a test script for the Codecademy anti_vowel exercise.

Created: 13/04/2015
Last Modified: 13/04/2015
"""

text = str(raw_input("Enter some text: "))
vowels = "aeiouAEIOU"


def anti_vowel(text):
	text_no_vowels = ""
	for letter in text:
		if letter not in vowels:
			text_no_vowels += letter	
	print text_no_vowels
anti_vowel(text)
