#!/usr/bin/env python3
import sys
fastaseq = open(sys.argv[1], "r")
genes = {}

for line in fastaseq:
	line = line.rstrip()
	if line[0]=='>':
		spacepos = line.find(' ')
		gene = line[:spacepos].strip('>')
		if gene not in genes.keys():
			genes[gene] = ''
	else:
		genes[gene] += line.strip('\n')
#definindo a quebra da sequência em códons usando for para adicionar as strings em uma lista
for gene in genes.keys():
	codons = []
	for i in range(0, len(genes[gene]), 3):
		codons.append(genes[gene][i:i+3])
	print(gene,'-frame-1-codons\n', *codons)

