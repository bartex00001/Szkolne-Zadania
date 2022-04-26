"""
wielomian:
y(x) = a*x^3 + b*x^2 + c*x + d

można zapisać jako:
y(x) = ((a*x + b)*x + c)*x + d

by obliczyć tak zapisany wielomian, przyjmijmy, że: 
coef = [a, b, c, d]		# wtedy coef[0] = a, coef[1] = b ...
x = [wczytana wartość]
wynik = 0	# taka zmienna istnieje

by obliczyć y(x) wykonamy następujące kroki:
wynik = coef[0]

wynik = wynik*x + coef[1]
wynik = wynik*x + coef[2]
wynik = wynik*x + coef[3]

po tych krokach: wynik = y(x), ale tylko dla wielomianu trzeciego stopnia

zapis w punktach dla wielomianu n-tego stopnia:
y(x) = a0 + a1 * x + a2 * x^2 + ... + an * x^n

coef = [an, ... , a2, a1, a0]
x = [wartosc liczbowa]

wynik = coef[0]

for i in range(n):
	wynik = wynik*x + coef[i+1]
"""

# Przykładowa implementacja w pliku schematHornera-normalnie.py