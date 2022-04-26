# Sprawdź czy wyraz jest palindromem

# Wczytaj wyraz
wyraz = input("Podaj wyraz: ")

# sprawdź czy odwrócony wyraz jest taki sam jak oryginalny
if wyraz == wyraz[::-1]:
    print("Wyraz jest palindromem")
else:
    print("Wyraz nie jest palindromem")
