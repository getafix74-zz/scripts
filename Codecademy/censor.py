#!/usr/bin/python

"""
This is my scratchpad for the Codecademy censor() exercise.

Created: 13/04/2015
Modified: 19/04/2015

"""
text = "The quick brown fox jumps over the lazy dog!"
word = "the"


def censor(text, word):
	word_letter_count = 0
	words = text.lower().split(" ")
	if word in words:
		for each_letter in word:
			word_letter_count += 1
			for word in words:
				word = "*" * word_letter_count
	print words				
censor(text,word)

"""
I couldn't find a decent solution but when I looked at the Q&A Forum I found this:
def censor(text, word):
	return text.replace(word, '*' * len(word))
"""
