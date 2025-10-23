x = int(input("Введіть число: "))

if 100 < x < 999 and x % 7 == 0:
    result = "Так"
else:
    result = "Ні"

print(result)
