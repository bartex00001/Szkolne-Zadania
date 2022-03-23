# Stworz dwie listy z wartosciami true/false i liste z suma bitowa (or)

import random

dlugosc = 10
arrA = []
arrB = []
arrSum = []

for i in range(dlugosc):
			   # random.randint(0, 1) -> losuje 1 albo 0 (prawda albo falsz)
	arrA.append( random.randint(0, 1) )
	arrB.append( random.randint(0, 1) )

print(arrA)
print(arrB)

for i in range(dlugosc):
				 # arrA[i] or arrB[i] -> suma logiczna (odpowiednik 'lub')
	arrSum.append( arrA[i] or arrB[i] )

print("Sumowa lista:")
print(arrSum)
