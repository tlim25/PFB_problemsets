#!/usr/bin/env python3
import sys

#Exercício 5
valor = sys.argv[1]

if valor == 1:
        print('O valor é igual a 1')
else:
        print ('O valor é diferente de 1')

#Exercício 7 e 9

valor2 = sys.argv[2]

if valor > 0:
        if valor < 50:
                print ('O valor é positivo e menor que 50')
        elif valor == 50:
                print ('O valor é igual a 50')
        else:
                print ('O valor é positivo e maior que 50')
elif valor < 0:
        print ('O valor é negativo')
else:
        print ('O valor é igual a zero')

if valor % 2 == 0:
        print ('O valor é par')
else:
        print ('O valor é ímpar')

if valor % 3 == 0:
        print ('O valor é divisível por 3')
else:
        print ('O valor não é divisível por 3')

