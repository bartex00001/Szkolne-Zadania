# Program sprawdzi czy z podanych długości odcinków można zbudować trójkąt
# Kiedy można? Gdy żadne dwa odcinki nie są krótsze niż trzeci:

# wczytaj długości trzech odcinków
a = int(input("Podaj długość pierwszego odcinka: "))
b = int(input("Podaj długość drugiego odcinka: "))
c = int(input("Podaj długość trzeciego odcinka: "))

# Sprawdz czy z odcinków a, b, c można zbudować trójkąt
if a + b > c and a + c > b and b + c > a:
    print("Z podanych odcinków można zbudować trójkąt")
else:
    print("Z podanych odcinków nie można zbudować trójta")
