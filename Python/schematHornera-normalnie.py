# Oblicz wielomian dla x i podanyc wspolczynników

# wprowadzanie danych
stopien = int (input("Podaj stopień wielomianu: ") )

podstawy = []

for i in range(stopien + 1):
    podstawy.append(int( input("Podaj podstawę przy " + stopień-i + " potędze: ") ))

x = int( input("Podaj niewiadomą x: ") )

# obliczanie wartosci wielomianu
value = podstawy[0]

for i in range(stopien):
    value = value*x + podstawy[i+1]

print(value)
