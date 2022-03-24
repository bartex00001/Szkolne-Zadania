# Program powinien stworzyć listę o 10 elementach, wypelnić ją wartościami z zakresu <1, 20> i Wypisac:
# min, max i średnia

import random	# importujemy bibliotekę liczb losowych

dlugosc = 10
lista = []

for i in range(dlugosc):
				# random.randint(1, 20) -> losowy int z przedziału <1, 20>
	lista.append( random.randint(1, 20) )

print(lista)

print("max: ", max(lista))
print("min: ", min(lista))

average = sum(lista) / dlugosc
print("avg: ", average)