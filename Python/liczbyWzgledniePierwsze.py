# Program sprawdzi czy liczby sa wzglednie piersze

def czyLiczbyWzgledniePierwsze(a, b):
    minimum = min(a, b)

    # Inna definicja liczb Względnie pierwszych:
    # Dwie liczby, które nie mają wspólnych dzielników
    for i in range(2, minimum+1):
        # Jeżeli jest wspólny dzielnik, to nie są względnie pierwsze
        if a % i == 0 and b % i == 0:
            return False
    return True

# Wczytaj dwie liczby całkowite
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

if czyLiczbyWzgledniePierwsze(a, b):
    print("Tak")
else:
    print("Nie")