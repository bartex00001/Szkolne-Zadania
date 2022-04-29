# Napisz program, który zamieni podaną literę, na drugą podaną literę

# Wczytaj litery (zamiana c1 na c2)
c1 = input("Podaj pierwsza litere: ")
c2 = input("Podaj druga litere: ")

# Wczytaj tekst do zamiany  liter
tekst = input("Podaj tekst: ")

# str nie można modyfikować elementów -> dodajemy do nowej listy
wynik = ""

for znak in tekst:
	if znak == c1:
		wynik += c2
	else:
		wynik += znak

print("Tekst po zamianie:", wynik)
