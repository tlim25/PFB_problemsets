#!/usr/bin/env python3
import re
with open("Python_07_nobody.txt") as file:
	contents = file.read()
	for line in contents:
		found = re.search(r"Nobody", contents)
		print(found)


