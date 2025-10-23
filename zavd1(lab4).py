
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))

S = a + b
D = a - b
P = a * b

if b != 0:
    Q = a / b
else:
    Q = "Ділення на нуль неможливе"

print(f"Сума: {S}")
print(f"Різниця: {D}")
print(f"Добуток: {P}")
print(f"Частка: {Q}")
