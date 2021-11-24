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
	reverseSeq.append(genes[gene][::-1])
	reverseSeq = ''.join(reverseSeq)
	for base in reverseSeq:
		complementSeq.append(complementBase[base])
	complementSeq = ''.join(complementSeq)
	for i in range (0, len(complementSeq), 3):
		complementar.append(complementSeq[i:i+3])
# definindo as traduções dos códons
	for codon in codons1:
		if len(codon) == 3:
			translation.append(translation_table[codon])
	for codon in complementar:
		if len(codon) == 3:
			translationComp.append(translation_table[codon])
	print(gene,'-frame1-translation','\n',*translation, sep='')
	print(gene,'-frame1-reverse complement translation','\n',*translationComp, sep='')

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
	for base in reverseSeq2:
		complementSeq2.append(complementBase[base])
	complementSeq2 = ''.join(complementSeq2)
	complementSeq2 = complementSeq2[0:len(complementSeq2)-1]
	for i in range (0, len(complementSeq2), 3):
		complementar2.append(complementSeq2[i:i+3])
	for codon in codons2:
		if len(codon) == 3:
			translation2.append(translation_table[codon])
	for codon in complementar2:
		if len(codon) == 3:
			translationComp2.append(translation_table[codon])
	print(gene,'-frame2-translation','\n',*translation2, sep='')
	print(gene,'-frame2-reverse complement translation','\n',*translationComp2, sep='')

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
	for base in reverseSeq3:
		complementSeq3.append(complementBase[base])
	complementSeq3 = ''.join(complementSeq3)
	complementSeq3 = complementSeq3[0:len(complementSeq3)-2]
	for i in range (0, len(complementSeq3), 3):
		complementar3.append(complementSeq3[i:i+3])
	for codon in codons3:
		if len(codon) == 3:
			translation3.append(translation_table[codon])
	for codon in complementar3:
		if len(codon) == 3:
                	translationComp3.append(translation_table[codon])
	print(gene,'-frame3-translation','\n',*translation3, sep='')
	print(gene,'-frame3-reverse complement translation','\n',*translationComp3, sep='')

