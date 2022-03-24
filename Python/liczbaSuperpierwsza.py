# program sprawdzi czy podana liczba jest super pierwsza

def isPrime(num):
    # Specjalny przypadek dla 1 i 0
    if num <= 1:
        return False

    # Sprawdź czy cos dzieli num (to można szybciej, ale nie trzeba)
    for it in range(2, num):
        if num % it == 0:
            return False

    # Nic nie dzieli liczby -> jest pierwsza
    return True

n = input("Podaj liczbe: ")
digitSum = 0

# Tutaj n jest tekstem (mozna iterowac)
for i in n:
    # i jest po kolei cyframi n (jako literki wiec trzeba zamienić na liczby korzystając z int() )
    digitSum += int(i)

# jeżeli n oraz [suma cyfr n] są pierwsze -> ok
if isPrime(int(n)) and isPrime(digitSum):
    print("YES")
else:
    print("NO")
