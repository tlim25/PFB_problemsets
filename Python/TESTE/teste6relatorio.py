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
#para determinar os aminoácidos que derivam dos códons em cada sequência, usamos um dicionário de tradução
translation_table = {
    'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
    'AAT':'N', 'AAC':'N',
    'GAT':'D', 'GAC':'D',
    'TGT':'C', 'TGC':'C',
    'CAA':'Q', 'CAG':'Q',
    'GAA':'E', 'GAG':'E',
    'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
    'CAT':'H', 'CAC':'H',
    'ATT':'I', 'ATC':'I', 'ATA':'I',
    'TTA':'L', 'TTG':'L', 'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
    'AAA':'K', 'AAG':'K',
    'ATG':'M',
    'TTT':'F', 'TTC':'F',
    'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S',
    'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'TGG':'W',
    'TAT':'Y', 'TAC':'Y',
    'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
    'TAA':'*', 'TGA':'*', 'TAG':'*'
}

#definindo a quebra das sequências em códons
for gene in genes.keys():
# no primeiro reading frame
	codons1 = []
	reverseSeq = []
	complementSeq = []
	complementar = []
	translation = []
	translationComp = []
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
# definindo as traduções dos códons
	for codon in codons1:
		if len(codon) == 3:
			translation.append(translation_table[codon])
	translation = ''.join(translation).split('M')
	longest = max(translation, key=len)
	print(gene,'-frame1-longest peptide\n',longest+'M')
	for codon in complementar:
		if len(codon) == 3:
			translationComp.append(translation_table[codon])
	translationComp = ''.join(translationComp).split('M')
	longestComp = max(translationComp, key=len)
	print(gene,'-frame1-comp-longest peptide\n',longestComp+'M')

#repetindo o processo para o segundo reading frame
	codons2 = []
	reverseSeq2 = []
	complementSeq2 = []
	complementar2 = []
	translation2 = []
	translationComp2 = []
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
	for codon in codons2:
		if len(codon) == 3:
			translation2.append(translation_table[codon])
	translation2 = ''.join(translation2).split('M')
	longest2 = max(translation2, key=len)
	print(gene,'-frame2-longest peptide\n',longest2+'M')
	for codon in complementar2:
		if len(codon) == 3:
			translationComp2.append(translation_table[codon])
	translationComp2 = ''.join(translationComp2).split('M')
	longestComp2 = max(translationComp2, key=len)
	print(gene,'-frame2-comp-longest peptide\n',longestComp2+'M')	

#repetindo o processo para o terceiro reading frame
	codons3 = []
	reverseSeq3 = []
	complementSeq3 = []
	complementar3 = []
	translation3 = []
	translationComp3 = []
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
	for codon in codons3:
		if len(codon) == 3:
			translation3.append(translation_table[codon])
	translation3 = ''.join(translation3).split('M')
	longest3 = max(translation3, key=len)
	print(gene,'-frame3-longest peptide\n',longest3+'M')
	for codon in complementar3:
		if len(codon) == 3:
			translationComp3.append(translation_table[codon])
	translationComp3 = ''.join(translationComp3).split('M')
	longestComp3 = max(translationComp3, key=len)
	print(gene,'-frame3-comp-longest peptide\n',longestComp3+'M')

