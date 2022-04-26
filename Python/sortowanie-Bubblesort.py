# Posortuj listę algorytmem Bubblesort
# Tak robimy tylko gdy nie można użyć funkcji sort()

# Bubble sort
def bubble_sort(lista):
    # Dla każdego pozycji w liście...
    for i in range(len(lista)):
        # Przejdz po wszystkich pozycjach...
        for j in range(len(lista) - 1):
            # Jeżeli element jest większy od elementu następnego - zamień miejscami
            if lista[j] > lista[j + 1]:
                # Zamień miejscami lista[j] i lista[j + 1]
                (lista[j], lista[j + 1]) = (lista[j + 1], lista[j])
    return lista

# Podaj długość listy
dlugosc = int(input("Podaj długość listy: "))

# Podaj elementy listy
lista = []
for i in range(dlugosc):
    lista.append(int(input("Podaj element listy: ")))

posortowanaLista = bubble_sort(lista)

# Wypisz posortowaną listę
print("Posortowana lista:\n", posortowanaLista)