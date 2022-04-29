# Program wypisze n-tą liczbę ciągu fibonacciego
# ciąg fibonacciego: 0, 1, 1, 2, 3, 5, 8, ...
# dla tej definicji pierwszym elementem ciągu jest 1

# Wczytaj n
n = int(input("Podaj ktora liczbe wypisac: "))

a = 0
b = 1

for i in range(n):
	a = a+b
	# zamien miejscami a i b
	(a, b) = (b, a)

print("N-ty wyraz ciagu:", a)