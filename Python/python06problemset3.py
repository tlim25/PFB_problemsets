#!/usr/bin/env python3

#Criamos um dicionário com os nt como chave, e o novo nt complementar como valor. Assim podemos usar o dicionário depois para substituir of valores.

complementBase = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
with open('Python_06.seq.txt', 'r') as file_object:
	for line in file_object:
#essa linha de código divide a string em duas na tabulação, assim temos uma string com a identificação e outra string com a sequência de bases
		ident,sequencia=line.rstrip().split('\t')
		reverseSeq = sequencia[::-1]
		print(f'{ident},{sequencia}')
		complementSeq = []
		for base in reverseSeq:
#Essa próxima linha imprime cada base da sequência, e, saparada por um tab, a base complementar usando a chave do dicionário
			#print(f'{base}\t{complementBase[base]}')
			complementSeq.append(complementBase[base])
		print(f'SeqComp:\t{"".join(complementSeq)}')
#AULA 28-10 AOS 6:45

