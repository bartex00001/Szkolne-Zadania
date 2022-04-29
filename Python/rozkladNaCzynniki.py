# Program wypisze rozklad na czynniki pierwsze liczby n

n = int(input("Podaj liczby: "))

listaCzynnikow = []

# Od pierwszej liczby pierwszej do potencjalnie maksymalnej (n)
for i in range(2, n+1):
	if n % i == 0:
		listaCzynnikow.append(i)

		# Usuwamy wielokrotności sprawdzanej liczby z rozkładu
		while n % i == 0:
			n //= i

print(listaCzynnikow)