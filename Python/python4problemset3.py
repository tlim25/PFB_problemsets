#!/usr/bin/env python3

print('IMPRIMINDO VALORES DE 1 A 100 USANDO WHILE')
n = 0
while n < 100:
	n += 1
	print(n)

print('IMPRIMINDO O FATORIAL DE 1000 USANDO WHILE')
fatorial = 1
z = 1000
while z > 0:
	fatorial = fatorial * z
	z -= 1
print(fatorial)

print('IMPRIMINDO VALORES PARES DA LISTA USANDO in')
lista = [101,2,15,22,95,33,2,27,72,15,52]
for n in lista:
	if n % 2 == 0:
		print (n)

print('IMPRIMINDO SOMA DE VALORES PARES E ÍMPARES USANDO for')
novalista = sorted(lista, key=None, reverse=False)
par = 0
impar = 0
for n in novalista:
	print(n, end=' ')
	if n % 2 == 0:
		par += n
	else:
		impar += n
print(f'Sum of even numbers: {par}\nSum of odd numbers: {impar}')

print('IMPRIMINDO VALORES DE 1 A 99 USANDO range')
for num in range(100):
	print(num, end = ' ')

print('IMPRIMINDO VALORES DE 1 A 100 USANDO list comprehension')
numeros = []
for num in range(101):
	numeros.append(num)
print(numeros)






	
