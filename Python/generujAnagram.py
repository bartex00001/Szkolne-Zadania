import random
from re import S

# Program wygeneruje anagram podanego słowa
# Anagram - słowo zawierające te same litery, ale w innej kolejności

# Wczytaj słowo
s = input("Podaj słowo: ")

# Najprostszy anagram - litery w odwrotnej kolejności
revS = s[::-1]

# Losowy anagram
trueAnagram = list(s)
for i in range(len(s)):
    # Wygeneruj losową liczbę z przedziału 0..len(s)-1
    r = random.randint(0, len(s) - 1)

    # Zamień s[i] na s[r]
    (trueAnagram[i], trueAnagram[r]) = (trueAnagram[r], trueAnagram[i])

# Wypisz anagramy
print("Odwrotny anagram:", revS)
print("Losowy anagram", trueAnagram) # to wypisze liste znaków (nie tekst)
