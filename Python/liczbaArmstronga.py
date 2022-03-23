# Sprawdz czy podana liczba jest 'armstrongowa'

strNum = input("Wprowadź liczbę: ")		# wczytujemy od uzytkownika liczbe JAKO TEKST
Num = int(strNum)						# przypisujemy zmiennej Num wczytana liczbe jako int

dlugosc = len(strNum)					# zapamietaj dlugosc (przyda sie pozniej)
suma = 0

for i in strNum:						# iterujemy po literach w tekscie
    suma += int(i) ** dlugosc			# dodajemy do sumy cyfre podniesiona do potegi dlugosci calej wprowadzonej liczby

if suma == Num:
	print("OK")
else:
	print("NO")