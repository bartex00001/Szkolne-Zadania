# W podanym tekście program policzy wystąpienia wskazanej litery

# Wczytaj tekst i literę
tekst = input("Podaj tekst: ")
litera = input("Podaj literę: ")

# Zlicz wystąpienia
licznik = 0

for znak in tekst:
    if znak == litera:
        licznik += 1

print("Liczba wystapien litery w tekscie:", licznik)
