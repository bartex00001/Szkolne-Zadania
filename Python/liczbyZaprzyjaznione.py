# Sprawdzenie czy dwie liczby są zaprzyjaźnione

def dzielniki(x):
    dziel = []

    for i in range(1, x):   # jest x bo chcemy tylko dzielnik właściwe tj. mniejszse od x
        if x%i == 0:
            dziel.append(i)

    return dziel

# Wprowadzenie danych
liczba1 = int(input("Podaj pierwszą liczbę: "))
liczba2 = int(input("Podaj drugą liczbę: "))

# sprawdzanie warunku liczb zaprzyjaźnionych
if sum(dzielniki(liczba1)) == liczba2 and sum(dzielniki(liczba2)) == liczba1:
    print("Liczby", liczba1, "i", liczba2, "są zaprzyjaźnione")
else:
    print("NIE")