# program sprawdzi czy podana liczba jest pierwsza

def isPrime(num):
    # Specjalny przypadek dla 1 i 0
    if num <= 1:
        return False

    # Sprawdz czy cos dzieli num (to mozna szybciej, ale nie trzeba)
    for it in range(2, num):
        if num % it == 0:
            return False

    # Nic nie dzieli liczby -> jest pierwsza
    return True

n = input()
digitSum = 0

# Tutaj n jest tekstem (mozna iterowac)
for i in n:
    # i jest po kolei cyframi n (jako literki wiec trezeba int())
    digitSum += int(i)

# jezeli n i [suma cyfr n] jest pierwsza -> ok
if isPrime(int(n)) and isPrime(digitSum):
    print("YES")
else:
    print("NO")
