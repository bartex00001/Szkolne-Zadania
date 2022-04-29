# wprowadzanie danych

stopien = int(input("Podaj stopień wielomianu: "))

podstawy = []

# iterujemy po pętli stopień+1 razy (bo współczynnik jest przy każdej potędze oraz jeden wolny), za każdym razem dodając nową wartość do listy
for i in range(stopien + 1):
    podstawy.append(int(input("Podaj podstawę przy " + str(stopien-i) + " potędze: ")))

#podajemy wartość x dla której obliczana jest wartośc wielomianu
x = int(input("Podaj niewiadomą x: "))


# obliczanie wartosci wielomianu
# patrz plik Teoria -> Horner

value = podstawy[0]

for i in range(stopien):
    value = value*x+podstawy[i+1]

print(value)

