#!/usr/bin/env python

import sys

#input comes from STDIN
for line in sys.stdin:

	#remove leading and trailing whitespaces
	line = line.strip()

	#split the line into words
	words = line.split()

	#increase counters
	for word in words:
		#write the results to STDOUT to be taken as input by the reducer
		print('%s\t%s' % (word, 1))

