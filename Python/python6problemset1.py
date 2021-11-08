#/!/usr/bin/env python3

file = open("Python_06.seq.txt", "r")
for line in file:
	line = line.rstrip()
	line = line.upper()
	print(line)


