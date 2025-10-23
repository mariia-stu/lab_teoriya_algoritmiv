vowels = "аеєиіїоуюяАЕЄИІЇОУЮЯ"  #українські голосні
latin = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"  #англійські літери

while True:
    S = input("Введіть речення українською мовою: ")

    #перевірка на наявність англійських символів
    if any(ch in latin for ch in S):
        print("Помилка! Введіть речення українською мовою!\n")
        continue
    else:
        break

#заміна
result = ""
for ch in S:
    if ch in vowels:
        result += "*"
    else:
        result += ch

n = len(S)

#результати
print(f"\nРезультат заміни: {result}")
print(f"Кількість символів: {n}")

