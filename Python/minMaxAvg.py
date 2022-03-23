# Program powinien stworzyc liste o 10 elementach, wypelnic ja wartosciami <1, 20> i sypisac:
# min, max i srednia

import random

dlugosc = 10
lista = []

for i in range(dlugosc):
				# random.randint(1, 20) -> losowy int w przedziale <1, 20>
	lista.append( random.randint(1, 20) )

print(lista)

print("max: ", max(lista))
print("min: ", min(lista))

average = sum(lista) / dlugosc
print("avg: ", average)