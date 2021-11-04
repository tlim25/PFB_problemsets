#!/usr/bin/env python3

favs = {}
favs['book'] = 'Bible'
favs['activity'] = 'sleeping'
favs['food'] = 'coffee'

print('Here is a list of values you can check: ')
for key in dict.keys(favs):
	print(key)
fav = input('What value do you want to check? ')
if fav in favs:
	print(favs[fav])

