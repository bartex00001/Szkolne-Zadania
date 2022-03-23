# policz silnie z liczby n

n = int(input("Podaj liczbe: "))
res = 1

for i in range(1, n+1):
    res *= i

print(res)
