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

# para determinar a sequência reversa complementar de cada sequência, podemos usar um dicionário com as substituições
complementBase = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

#definindo a quebra das sequências em códons
for gene in genes.keys():
# no primeiro reading frame
	codons1 = []
	reverseSeq = []
	complementSeq = []
	complementar = []
	for i in range(0, len(genes[gene]), 3):
		codons1.append(genes[gene][i:i+3])
# definindo a sequência reversa
	reverseSeq.append(genes[gene][::-1])
	reverseSeq = ''.join(reverseSeq)
# caso não haja um códon completo ao final da sequência codons1, desconsideraremos esses nucleotídeos para escrever a reversa complementar
	if len(codons1[len(codons1)-1]) == 1:
		reverseSeq = reverseSeq[1:]
	elif len(codons1[len(codons1)-1]) == 2:
		reverseSeq = reverseSeq[2:]
#usando o dicionário para estabelecer a fita complementar
	for base in reverseSeq:
		complementSeq.append(complementBase[base])
# transformando complementSeq em uma única string e usando-a para criar a lista complementar com a sequência separada em códons
	complementSeq = ''.join(complementSeq)
	for i in range (0, len(complementSeq), 3):
		complementar.append(complementSeq[i:i+3])
	print(gene,'-frame1-codons')
	print(*codons1)
	print(gene,'-frame1-reversecomp')
	print(*complementar)

#repetindo o processo para o segundo reading frame
	codons2 = []
	reverseSeq2 = []
	complementSeq2 = []
	complementar2 = []
	for i in range(1, len(genes[gene]), 3):
		codons2.append(genes[gene][i:i+3])
	reverseSeq2.append(genes[gene][::-1])
	reverseSeq2 = ''.join(reverseSeq2)
	if len(codons2[len(codons2)-1]) == 1:
		reverseSeq2 = reverseSeq2[1:]
	elif len(codons2[len(codons2)-1]) == 2:
		reverseSeq2 = reverseSeq2[2:]
	for base in reverseSeq2:
		complementSeq2.append(complementBase[base])
	complementSeq2 = ''.join(complementSeq2)
	for i in range (0, len(complementSeq2), 3):
		complementar2.append(complementSeq2[i:i+3])
	print(gene,'-frame2-codons')
	print(*codons2)
	print(gene,'-frame2-reversecomp')
	print(*complementar2)

#repetindo o processo para o terceiro reading frame
	codons3 = []
	reverseSeq3 = []
	complementSeq3 = []
	complementar3 = []
	for i in range(2, len(genes[gene]), 3):
		codons3.append(genes[gene][i:i+3])
	reverseSeq3.append(genes[gene][::-1])
	reverseSeq3 = ''.join(reverseSeq3)
	if len(codons3[len(codons3)-1]) == 1:
		reverseSeq3 = reverseSeq3[1:]
	elif len(codons3[len(codons3)-1]) == 2:
		reverseSeq3 = reverseSeq3[2:]
	for base in reverseSeq3:
		complementSeq3.append(complementBase[base])
	complementSeq3 = ''.join(complementSeq3)
	for i in range (0, len(complementSeq3), 3):
		complementar3.append(complementSeq3[i:i+3])
	print(gene,'-frame3-codons')
	print(*codons3)
	print(gene,'-frame3-reversecomp')
	print(*complementar3)

