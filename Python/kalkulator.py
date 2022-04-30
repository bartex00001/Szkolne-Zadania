# program imitujący prosty kalkulator.
# Wprowadza się pierwszą liczbę, następnie działanie i drugą liczbę

liczba1 = float(input("Podaj wartość: "))   #wprowadzenie pierwszej wartości

while True:     # Nieskończona pętla
    dzialanie = input("Podaj działanie do wykonania ( *, /, +, - lub quit ): ")

    if dzialanie == "quit":     # Sposób na wyłączenie programu
        break
    
    liczba2 = float(input("Podaj kolejną wartość: "))


    if dzialanie == "+":
        liczba1 = liczba1 + liczba2
    elif dzialanie == "-":
        liczba1 = liczba1 - liczba2
    elif dzialanie == "*":
        liczba1 = liczba1 * liczba2
    elif dzialanie == "/":
        if liczba2 == 0:
            print("BŁĄD DZIELENIA PRZEZ ZERO")
        else:
            liczba1 = liczba1 / liczba2

    print(liczba1)
    