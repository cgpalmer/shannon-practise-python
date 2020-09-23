codon = ["a", "u", "g", "c"]

x = 0
y = 0

for j in range(4):
    for k in range(4):
        print(codon[x], codon[y], codon[0])
        for i in range(3):
            print(codon[x], codon[y], codon[i+1])
        y = y + 1
    x = x + 1
    y = 0

