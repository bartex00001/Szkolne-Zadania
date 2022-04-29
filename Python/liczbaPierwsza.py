# Program sprawdzi czy podana liczba jest liczbą pierwszą

def czyLiczbaPierwsza(liczba):
    # Tylko liczby większe od 1 mogą być pierwsze
    if liczba <= 1:
        return False
    
    for i in range(2, liczba):
        if liczba % i == 0:
            return False    # jeżeli liczba ma jakiekolwiek dzielniki większe od 2 i mniejsze od niej samej to nie jest pierwsza
    return True

n = int(input("Podaj liczbę: "))

if czyLiczbaPierwsza(n):
    print("Liczba jest liczbą pierwszą")
else:
    print("Liczba nie jest liczbą pierwszą")
