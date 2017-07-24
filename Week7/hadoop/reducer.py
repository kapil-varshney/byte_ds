#!/usr/bin/env python

from operator import itemgetter
import sys

current_word = None
current_count = 0
word= None

#input comes from STDIN
for line in sys.stdin:

	#remove leading and trailing whitespaces
	line = line.strip()

	# parse the input we got from the mapper.py
	word, count = line.split('\t', 1)

	# convert count (currently a string) to int
	try:
		count = int(count)
	except ValueError:
		continue

	if current_word == word:
		current_count += count
	else:
		if current_word:
			print('%s\t%s' % (current_word, current_count))
		current_count = count
		current_word = word

if current_word == word:
	print('%s\t%s' % (current_word, current_count))
