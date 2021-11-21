#!/usr/bin/env python3
import sys

# recebendo o arquivo do input
fastaseq = open(sys.argv[1], "r")

# definindo oa dicionários para receber os dados
genes = {}
nucleotide = {}

for line in fastaseq:
	line = line.rstrip()
# removendo as informações da linha da descrição para obter apenas a identificação do gene
# para isso, considerei apenas os caracteres antes do primeiro espaço, e ignorando o '>'
	if line[0]=='>':
		spacepos = line.find(' ')
		gene = line[:spacepos].strip('>')
#atribuindo os genes como chaves no dicionário
		if gene not in genes.keys():
			genes[gene]=''
#juntando as linhas da sequência em uma única string e atribuindo o valor para a chave do respectivo gene
	else:
		genes[gene]+= line.strip('\n')
#fazendo a contagem de nucleotídeos, adicionando cada nt como chave e sua contagem como valor associado
for gene in genes.keys():
	for nt in set(genes[gene]):
		if gene not in nucleotide.keys():
			nucleotide[gene] = {}
		nucleotide[gene][nt] = genes[gene].count(nt)
#imprimindo as informaçõs no formato seqName\tA_count\tT_count\tC_count\G_count como sugerido pelo exercício
	print(gene,'\t',nucleotide[gene]['A'],'\t',nucleotide[gene]['T'],'\t',nucleotide[gene]['C'],'\t',nucleotide[gene]['G'])

