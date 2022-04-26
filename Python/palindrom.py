# Sprawdź czy wyraz jest palindromem

# Wczytaj wyraz
wyraz = input("Podaj wyraz: ")

# sprawdź czy odwrócony wyraz jest taki sam jak oryginalny
if wyraz == wyraz[::-1]:
    print("Wyraz jest palindromem")
else:
    print("Wyraz nie jest palindromem")


# Alternatywnie - sprawdzanie w funkcji
def czyPalindrom(word):
    # Tutaj zwracamyh True/False, albo wypisujemy komunikat
    return word == word[::-1]

if czyPalindrom(wyraz):
    print("Wyraz jest palindromem - z funkcji")
else:
    print("Wyraz nie jest palindromem - z funkcji")
