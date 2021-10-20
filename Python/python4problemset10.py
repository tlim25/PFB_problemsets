#!/usr/bin/env python3
import sys

valor1 = int(sys.argv[1])
valor2 = int(sys.argv[2])
valor3 = int(sys.argv[3])
valor4 = int(sys.argv[4])

for num in range(valor1, valor2+1):
	print(num)

for num in range (valor3, valor4+1):
	if num % 2 == 0:
		print (num)
