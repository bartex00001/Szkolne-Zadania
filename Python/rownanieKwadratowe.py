# Program wyznaczy rozwiązanie równania kwadratowego, dla podanych współczynników a, b, c.

from math import sqrt # z modułu math importujemy funkcję sqrt (pierwiastek kwadratowy)

# Wprowadzanie danych
a = int(input("Podaj współczynnik 'a': "))
b = int(input("Podaj współczynnik 'b': "))
c = int(input("Podaj współczynnik 'c': "))

# Obliczmay deltę (jak na matematyce)
delta = b*b - 4*a*c

# Rozważamy przypadki dla różnych wartości delty
if delta > 0:
    x1 = (-b-sqrt(delta)) / (2*a)
    x2 = (-b+sqrt(delta)) / (2*a)

    print("Miejsca zerowe to", x1, "i", x2)
elif delta == 0:
    x = -b / (2*a)

    print("Jest tylko jedno miejce zerowe:", x)
elif delta < 0:
    print("Brak rozwiązań w liczbach rzeczywistych")
