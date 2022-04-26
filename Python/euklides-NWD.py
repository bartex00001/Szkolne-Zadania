# Program policzy nwd dla dwóch liczb a i b

# To implementacja algorytmu euklidesa
def nwd(a, b):
    if a % b == 0:
        return b
    else:
        return nwd(b, a % b)

# Wczytaj dwie liczby n1 i n2
n1 = int(input("Podaj pierwszą liczbę: "))
n2 = int(input("Podaj drugą liczbę: "))

print("NWD podanych liczb:", nwd(n1, n2))