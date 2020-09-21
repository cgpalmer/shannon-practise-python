firstLetter = ["a", "u", "g", "c"]

# thirdLetter = ["a", "u", "g", "c"]
# x = 0

# for letter in firstLetter:
#     print(letter,secondLetter[x],thirdLetter[x])
#     x = x+1

# for letter in secondLetter:
#     print(letter,secondLetter[0],thirdLetter[0])


# print(firstLetter[0]*2,firstLetter[0])
# print(firstLetter[1]*2,firstLetter[1])
# print(firstLetter[2]*2,firstLetter[2])
# print(firstLetter[3]*2,firstLetter[3])

# print(firstLetter[0]*2,firstLetter[1])
# print(firstLetter[0]*2,firstLetter[2])
# print(firstLetter[0]*2,firstLetter[3])

# print(firstLetter[1]*2,firstLetter[0])
# print(firstLetter[1]*2,firstLetter[2])
# print(firstLetter[1]*2,firstLetter[3])

# print(firstLetter[2]*2,firstLetter[0])
# print(firstLetter[2]*2,firstLetter[1])
# print(firstLetter[2]*2,firstLetter[3])

# print(firstLetter[3]*2,firstLetter[0])
# print(firstLetter[3]*2,firstLetter[1])
# print(firstLetter[3]*2,firstLetter[2])

# print(firstLetter[0],firstLetter[1]*2)
# print(firstLetter[0],firstLetter[2]*2)
# print(firstLetter[0],firstLetter[3]*2)

# print(firstLetter[1],firstLetter[0]*2)
# print(firstLetter[1],firstLetter[2]*2)
# print(firstLetter[1],firstLetter[3]*2)

# print(firstLetter[2],firstLetter[0]*2)
# print(firstLetter[2],firstLetter[1]*2)
# print(firstLetter[2],firstLetter[3]*2)

# print(firstLetter[3],firstLetter[0]*2)
# print(firstLetter[3],firstLetter[1]*2)
# print(firstLetter[3],firstLetter[2]*2)

# print(firstLetter[0],firstLetter[1],firstLetter[0])
# print(firstLetter[0],firstLetter[2],firstLetter[0])
# print(firstLetter[0],firstLetter[3],firstLetter[0])

# print(firstLetter[1],firstLetter[0],firstLetter[1])
# print(firstLetter[1],firstLetter[2],firstLetter[1])
# print(firstLetter[1],firstLetter[3],firstLetter[1])

# print(firstLetter[2],firstLetter[0],firstLetter[2])
# print(firstLetter[2],firstLetter[1],firstLetter[2])
# print(firstLetter[2],firstLetter[3],firstLetter[2])

# print(firstLetter[3],firstLetter[0],firstLetter[3])
# print(firstLetter[3],firstLetter[1],firstLetter[3])
# print(firstLetter[3],firstLetter[2],firstLetter[3])

# # secondLetter = ["a", "u", "g", "c"]

# print(firstLetter[0],firstLetter[1],firstLetter[2])
# print(firstLetter[0],firstLetter[1],firstLetter[3])
# print(firstLetter[0],firstLetter[2],firstLetter[1])
# print(firstLetter[0],firstLetter[2],firstLetter[3])
# print(firstLetter[0],firstLetter[3],firstLetter[1])
# print(firstLetter[0],firstLetter[3],firstLetter[2])

# print(firstLetter[1],firstLetter[0],firstLetter[2])
# print(firstLetter[1],firstLetter[0],firstLetter[3])
# print(firstLetter[1],firstLetter[2],firstLetter[0])
# print(firstLetter[1],firstLetter[2],firstLetter[3])
# print(firstLetter[1],firstLetter[3],firstLetter[2])
# print(firstLetter[1],firstLetter[3],firstLetter[0])

# print(firstLetter[2],firstLetter[0],firstLetter[1])
# print(firstLetter[2],firstLetter[0],firstLetter[3])
# print(firstLetter[2],firstLetter[1],firstLetter[0])
# print(firstLetter[2],firstLetter[1],firstLetter[3])
# print(firstLetter[2],firstLetter[3],firstLetter[1])
# print(firstLetter[2],firstLetter[3],firstLetter[0])

# print(firstLetter[3],firstLetter[0],firstLetter[2])
# print(firstLetter[3],firstLetter[0],firstLetter[1])
# print(firstLetter[3],firstLetter[2],firstLetter[0])
# print(firstLetter[3],firstLetter[2],firstLetter[1])
# print(firstLetter[3],firstLetter[1],firstLetter[2])
# print(firstLetter[3],firstLetter[1],firstLetter[0])

for x in range(4):
    for i in range(4):
        print(firstLetter[x]*2,firstLetter[i])
        if firstLetter[i] != firstLetter[x]:
            print(firstLetter[x],firstLetter[i]*2)
            print(firstLetter[x],firstLetter[i],firstLetter[x])
    

