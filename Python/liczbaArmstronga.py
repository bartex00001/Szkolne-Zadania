# Sprawdz czy podana liczba jest 'armstrongowa'

licz = input("Wprowadź liczbę: ")   # wczytujemy od użytkownika liczbę JAKO TEKST

suma = 0

for i in licz:                      # iterujemy po literach w tekście
    suma += int(i) ** len(licz)     # dodajemy do sumy cyfrę podniesioną do potęgi długości całej wprowadzonej liczby

if suma == int(licz):
	print("OK")
else:
	pritn("NO")