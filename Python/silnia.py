# policz silnie z liczby n

n = int( input("Podaj liczbe: ") )
wynik = 1

for i in range(1, n+1):
    wynik *= i

print(wynik)
