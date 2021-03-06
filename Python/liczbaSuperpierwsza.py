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

# Można tak zrobić, bo n jest tekstem
for cyfra in n:
    # cyfra jest tekstem (bo bieżemy z tekstu), dlatego trzeba zamienić na int
    digitSum += int(cyfra)

# jeżeli n oraz [suma cyfr n] są pierwsze -> ok
if isPrime(int(n)) and isPrime(digitSum):
    print("YES")
else:
    print("NO")
