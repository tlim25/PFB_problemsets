#!/usr/bin/env python3


linecount = 0
charactercount = 0

with open('Python_06.fastq') as fileobj:
	for line in fileobj:
		linecount += 1
		characterline = len(line)
		charactercount += characterline
	print(f'Number of lines: {linecount}\nTotal number of characters: {charactercount}\nAverage line length: {charactercount/linecount}')

