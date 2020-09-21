import re
import json

aminoAcid = """{
    "AUG": "Methonine"
    "UUU": 
    "UUC":
    "UUA":
    "UUG":
    'CUU':
    'CUC':
    'CUA':
    'CUG':
    'AUU':
    'AUC':
    'AUA':
    'GUU':
    'GUC':
    'GUA':
    'GUG':
    'UCU':
    'UCC':
    'UCA':
    'UCG':
    'CCU':
    'CCC':
    'CCA':
    'CCG':

}"""







aminoSearch = json.loads(aminoAcid)


def fasterFindCodons(rna):
    new_method = re.findall('.{1,3}', rna)
    return(new_method)


rna = 'augcgcugaagucagugucaggac'
stopCodon = ['UAA', 'UAG', 'UGA']

codons = fasterFindCodons(rna)

def matchAminoAcids(codons):
    for codon in codons:
        if codon in aminoSearch:
            print("success")
            print(aminoSearch[codon])
        else:
            print("Not in database...yet")

matchAminoAcids(codons)
'''
Find all the codons

First function
is first codon !aug = error in sequence
else remove from sequence and continue

Second function
Loop through codons
    if codon = stop codon then aminoAcid = STOP

Third Function
if first letter  = a g u c then give respective value 
return first letter

Forth Function
if the second letter is 

'''






