# uzyskanie wszystkich dzielników liczby
def dzielniki(x):
    dziel = []

    for i in range(1, x):   # jest x bo chcemy tylko dzielnik właściwe tj. mniejszse od x
        if x%i == 0:
            dziel.append(i)

    return dziel


liczba = int(input("Podaj liczbę do sprawdzenia: "))
if liczba == sum(dzielniki(liczba)):
    print("Liczba doskonała")
else:
    print("Liczba NIE doskonała")