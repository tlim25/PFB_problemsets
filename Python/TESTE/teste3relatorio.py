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
		spacepos = line.find(' ')
		gene = line[:spacepos].strip('>')
# atribuindo os genes como chaves no dicionário
		if gene not in genes.keys():
			genes[gene] = ''
#juntando as linhas da sequence em uma única string e atribuindo o valor para a chave do respectivo gene
	else:
		genes[gene] += line.strip('\n')
#definindo a quebra da sequência em códons usando for para adicionar as strings em uma lista
for gene in genes.keys():
# no primeiro reading frame
	codons1 = []
	frame1 = 0
	for i in range(frame1, len(genes[gene]), 3):
		codons1.append(genes[gene][i:i+3])
	print(gene,f'-frame-{frame1+1}-codons')
	print(*codons1)
#no segundo reading frame
	codons2=[]
	frame2 = 1
	for i in range(frame2, len(genes[gene]),3):
		codons2.append(genes[gene][i:i+3])
	print(gene, f'-frame-{frame2+1}-codons')
	print(*codons2)
# no terceiro reading frame
	codons3 = []
	frame3 = 2
	for i in range(frame3, len(genes[gene]), 3):
		codons3.append(genes[gene][i:i+3])
	print(gene, f'-frame-{frame3+1}-codons')
	print(*codons3)

