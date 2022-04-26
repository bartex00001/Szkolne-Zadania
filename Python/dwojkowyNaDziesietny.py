# Program zamieni zapis w systmemie dwojkowym na dziesiętny

# Wczytaj binarną liczbę jako tekst
liczbaBinarna = input("Podaj liczbę dwójkową: ")

wynik = 0

# zaczynamy od najbardziej znaczącego bitu -> start = 2^(len-1)
potega = 2 ** (len(liczbaBinarna)-1)

for cyfra in liczbaBinarna:
    # Dodajemy tylko przy jedynce
    if cyfra == "1":
        wynik += potega
    
    # Idziemy do mniej znaczących bitów
    potega /= 2

print("Wynik:", wynik)