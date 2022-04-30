# Program wypisze wszystkie dzielnikin podanej liczby

def dzielniki(x):
    dziel = []

    for i in range(1, x+1): # jest x+1 bo sama liczba też jest swoim dzielnikiem
        if x%i == 0:
            dziel.append(i)

    return dziel

print(dzielniki(int( input("Podaj liczbę której dzielniki mają być wypisane: ")) ))