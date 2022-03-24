# Sprawdź czy podana liczba jest liczbą Armstronga

strNum = input("Wprowadź liczbę: ")		# wczytujemy od użytkownika liczbę JAKO TEKST
Num = int(strNum)						# przypisujemy zmiennej Num wczytaną liczbę jako int

dlugosc = len(strNum)					# zapamietujemy dlugość (przyda się później)
suma = 0

for i in strNum:						# iterujemy po literach w tekście
    suma += int(i) ** dlugosc			# dodajemy do sumy cyfrę podniesioną do potęgi długości całej wprowadzonej liczby

if suma == Num:
	print("TAK")
else:
	print("NIE")