tab = [[1,   2,  3,  4,  5],
	   [6,   7,  8,  9, 10],
	   [11, 12, 13, 14, 15],
	   [16, 17, 18, 19, 20],
	   [21, 22, 23, 24, 25]]

# wypisywanie wszytkich wartości w tablicy, każda w nowej linii
for row in tab:
	for element in row:
		print(element)

print("Pozycja 4, 3: ")
print(tab[3][2]) # wypisywanie na pozycji 4 w dół 3 w prawo (bo zaczynamy od 0) w tym przypadku 18

print("Przekątna: ")

# wypisywanie na przekątnej
for i in range(len(tab)):
	print(tab[i][i])
	