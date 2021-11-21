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

# para determinar a sequência reversa complementar de cada sequência, podemos usar um dicionário com as substituições
complementBase = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

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
# caso não haja um códon completo (3 nt) ao final da sequência codons1, desconsideraremos esses nucleotídeos para escrever a reversa complementar
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
	print(gene,'-frame1-codons\n',*codons1)
	print(gene,'-frame1-reversecomp\n',*complementar)

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
	print(gene,'-frame2-codons\n',*codons2)
	print(gene,'-frame2-reversecomp\n',*complementar2)

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
	print(gene,'-frame3-codons\n',*codons3)
	print(gene,'-frame3-reversecomp\n',*complementar3)

