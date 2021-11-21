#!/usr/bin/env python3
import sys

# recebendo o arquivo do input
fastaseq = open(sys.argv[1], "r")

#definindo o dicionário para receber os dados
genes = {}

for line in fastaseq:
	line = line.rstrip()
# removendo as informações da linha da descrição para obter apenas a identificação do gene
# para isso, considerei apenas os caracteres antes do primeiro espaço, e ignorando o '>'
	if line[0]=='>':
		spacepos = line.find(' ') #posição do primeiro espaço
		gene = line[:spacepos].strip('>')
#atribuindo os genes como chaves no dicionário
		if gene not in genes.keys():
			genes[gene] = ''
# juntando as linhas da sequência em uma única string e atribuindo o valor para a chave do respectivo gene
	else:
		genes[gene] += line.strip('\n')
#definindo a quebra da sequência em códons usando for para adicionar as strings em uma lista
for gene in genes.keys():
	codons = []
	frame = 0
	for i in range(frame, len(genes[gene]), 3):
		codons.append(genes[gene][i:i+3])
	print(gene,f'-frame-{frame+1}-codons')
	print(*codons)

