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
# no primeiro reading frame
	codons1 = []
	for i in range(0, len(genes[gene]), 3):
		codons1.append(genes[gene][i:i+3])
	print(gene,'-frame1-codons\n', *codons1)
#no segundo reading frame
	codons2=[]
	for i in range(1, len(genes[gene]),3):
		codons2.append(genes[gene][i:i+3])
	print(gene,'-frame2-codons\n', *codons2)
# no terceiro reading frame
	codons3 = []
	for i in range(2, len(genes[gene]), 3):
		codons3.append(genes[gene][i:i+3])
	print(gene,'-frame3-codons\n', *codons3)

