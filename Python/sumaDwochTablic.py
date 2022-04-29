# Stwórz dwie listy losowymi wartościami i je dodaj

import random

dlugosc = 10
arrA = []
arrB = []
arrSum = []

# wypełnienie dwóch pierwszych list
for i in range(dlugosc):
			   # random.randint(0, 9) -> losuje liczby od 0 do 9
	arrA.append( random.randint(0, 9) )
	arrB.append( random.randint(0, 9) )

print(arrA)
print(arrB)


for i in range(dlugosc):
	arrSum.append(arrA[i] + arrB[i])

print(arrSum)