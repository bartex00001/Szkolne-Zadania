# Program szyfrujący i odszyfrujący tekst za pomocą algorytmu Cezara

def zaszyfrujTekst(tekst, klucz):
    zaszyfrowanyTekst = ""
    
    for znak in tekst:
        # isalpha - sprawdza czy znak jest literą
        if znak.isalpha():
            if znak.isupper():
                znak = chr((ord(znak) + klucz - 65) % 26 + 65)
            else:
                znak = chr((ord(znak) + klucz - 97) % 26 + 97) 

        # dodajemy znak do zaszyfrowanego tekstu
        zaszyfrowanyTekst += znak
    return zaszyfrowanyTekst


def odszyfrujTekst(tekst, klucz):
    odszyfrowanyTekst = ""

    for znak in tekst:
        if znak.isalpha():
            if znak.isupper():
                znak = chr((ord(znak) - klucz - 65) % 26 + 65)
            else:
                znak = chr((ord(znak) - klucz - 97) % 26 + 97) 

        odszyfrowanyTekst += znak
    return odszyfrowanyTekst

# wczytaj tekst i klucz
tekst = input("Podaj tekst: ")
klucz = int(input("Podaj klucz: "))

