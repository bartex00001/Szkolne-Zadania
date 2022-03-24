# policz silnię liczby n

n = int( input("Podaj liczbe: ") )
wynik = 1

for i in range(1, n+1):     # range(1, n+1) jest dlatego, że normalnie range(a) zaczyna od zera i nie uwzględnia a
    wynik *= i

print(wynik)
