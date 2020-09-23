import re
import json

aminoAcid = """{
    "GCU":"alanine ",
    "GCC":"alanine ",
    "GCA":"alanine ",
    "GCG":"alanine ",
    "AGA":"arginine ",
    "AGG":"arginine ",
    "CGU":"arginine ",
    "CGC":"arginine ",
    "CGA":"arginine ",
    "CGG":"arginine ",
    "AAU":"asparagine ",
    "AAC":"asparagine ",
    "GAU":"aspartic acid ",
    "GAC":"aspartic acid ",
    "UGU":"cysteine ",
    "UGC":"cysteine ",
    "CAA":"glutamine ",
    "CAG":"glutamine ",
    "GAA":"glutamic acid ",
    "GAG":"glutamic acid ",
    "GGU":"glycine ",
    "GGC":"glycine ",
    "GGA":"glycine ",
    "GGG":"glycine ",
    "CAU":"histidine ",
    "CAC":"histidine ",
    "AUU":"isoleucine ",
    "AUC":"isoleucine ",
    "AUA":"isoleucine ",
    "UUA":"leucine ",
    "UUG":"leucine ",
    "CUU":"leucine ",
    "CUC":"leucine ",
    "CUA":"leucine ",
    "CUG":"leucine ",
    "AAA":"lysine ",
    "AAG":"lysine ",
    "AUG":"methionine ",
    "UUU":"phenylalanine ",
    "UUC":"phenylalanine ",
    "CCU":"proline ",
    "CCC":"proline ",
    "CCA":"proline ",
    "CCG":"proline ",
    "AGU":"serine ",
    "AGC":"serine ",
    "UCU":"serine ",
    "UCC":"serine ",
    "UCA":"serine ",
    "UCG":"serine ",
    "ACU":"threonine ",
    "ACC":"threonine ",
    "ACA":"threonine ",
    "ACG":"threonine ",
    "UGG":"tryptophan ",
    "UAU":"tyrosine ",
    "UAC":"tyrosine ",
    "GUU":"valine ",
    "GUC":"valine ",
    "GUA":"valine ",
    "GUG":"valine ",
    "UAA":"STOP ",
    "UAG":"STOP ",
    "UGA":"STOP "
}"""

aminoSearch = json.loads(aminoAcid)


def fasterFindCodons(rna):
    new_method = re.findall('.{1,3}', rna)
    return(new_method)


rna = input("Paste in your RNA here:")

codons = fasterFindCodons(rna)
aminoAcidList = []


def matchAminoAcids(codons):
    for codon in codons:
        if codon in aminoSearch:
            aminoAcidList.append(aminoSearch[codon])
    print(aminoAcidList)


matchAminoAcids(codons)
