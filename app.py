import re
import json

aminoAcid = """{
    "aug": "Methonine"
}"""

aminoSearch = json.loads(aminoAcid)


def fasterFindCodons(rna):
    new_method = re.findall('.{1,3}', rna)
    return(new_method)


rna = 'augcgcugaagucagugucaggac'
stopCodon = ['UAA', 'UAG', 'UGA']

keyVal = fasterFindCodons(rna)
print(keyVal)

startCodon = keyVal[0]
print(startCodon)

if startCodon in aminoSearch:
    print("success")
    print(aminoSearch[startCodon])

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






