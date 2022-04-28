# Posortuj listę algorytmem Bubblesort
# Tak robimy tylko gdy nie można użyć funkcji sort()

# Bubble sort
def bubble_sort(li):
    # Dla każdego pozycji w liście...
    for i in range(len(li)):
        # Przejdz po wszystkich pozycjach...
        for j in range(len(li) - 1):
            # Jeżeli element jest większy od elementu następnego - zamień miejscami
            if li[j] > li[j + 1]:
                # Zamień miejscami li[j] i li[j + 1]
                (li[j], li[j + 1]) = (li[j + 1], li[j])

    # nie zwracamy li, bo jest to referencja - jej zmiana zmienia orginał

# Podaj długość listy
dlugosc = int(input("Podaj długość listy: "))

# Podaj elementy listy
lista = []
for i in range(dlugosc):
    lista.append(int(input("Podaj element listy: ")))

bubble_sort(lista)

# Wypisz posortowaną listę
print("lista:\n", lista)
