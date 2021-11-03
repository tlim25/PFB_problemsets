#!usr/bin/env python3

dna_list = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
lengths = [len(dna) for dna in dna_list]

for dna in dna_list:
	print(len(dna), '	',dna)

tuples = list(zip(lengths, dna_list))
print(tuples)
for length, sequence in tuples:
	print(length,'	', sequence)


