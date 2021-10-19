#!/usr/bin/env python3

taxa = 'sapiens,erectus,neanderthalensis'
print(taxa)
print (taxa[1])

species = taxa.split(',')
print(species)

sorted(species, key=None, reverse=False)

sorted(species, key=len, reverse=False)
