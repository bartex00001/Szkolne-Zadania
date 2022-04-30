# program imitujący prosty kalkulator.
# Wprowadza się pierwszą liczbę, następnie działanie i drugą liczbę

liczba1 = float(input("Podaj pierwsza liczbe: "))

dzialanie = input("Podaj działanie do wykonania ( *, /, +, - ): ")
    
liczba2 = float(input("Podaj droga liczbe: "))

print("wynik:") # Ładne formatowanie wyjścia
# wybór działania
if dzialanie == "+":
    print(liczba1 + liczba2)
elif dzialanie == "-":
    print(liczba1 - liczba2)
elif dzialanie == "*":
    print(liczba1 * liczba2)
elif dzialanie == "/":
    if liczba2 != 0:
        print(liczba1 / liczba2)   
    else:
         print("BŁĄD DZIELENIA PRZEZ ZERO")
    