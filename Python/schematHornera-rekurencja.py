# Oblicz wielomian dla x i podanyc wspolczynników REKURENCYJNIE - trudniejsza wersja

def liczHorner(stopien):
	# koniec rekurencji? daj 0, bo 0 * x = 0
	if stopien == ileWspolczynnikow:
		return 0

	return coeff[stopien] + liczHorner(stopien+1)*x

# Wspolczynnikow jest o jeden wiecej niz stopien
ileWspolczynnikow = int(input("podaj stopien wilomianu: ")) + 1
# coeff[i] jest przy x do potęgi i
coeff = []

for i in range(ileWspolczynnikow):
	coeff.append(int( input("wsp. przy x do pot." + str(i) +  ": ") ))

x = int(input("podaj x: "))

# Zaczynamy od zewnątrz (x^0)
print(liczHorner(0))