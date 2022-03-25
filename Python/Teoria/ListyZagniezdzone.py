tab = [[1,   2,  3,  4,  5],
	   [6,   7,  8,  9, 10],
	   [11, 12, 13, 14, 15],
	   [16, 17, 18, 19, 20],
	   [21, 22, 23, 24, 25]]

# wypisywanie wszytkich wartości w tablicy
'''for i in tab:
	for j in i:
		print(j)

# alternatywnie
for i in range(len(tab)):
	for j in range(len(tab[i])):
		print( tab[i][j] )'''

# print(tab[3][2]) # wypistywanie na pozycji 4 w dół 3 w prawo

# wypisywanie na przekątnej
for i in range(len(tab)):
	print(tab[i][i])
	