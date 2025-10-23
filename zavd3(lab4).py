
N = int(input("Введіть число N: "))

result = []

for i in range(1, N + 1):
    if i % 4 == 0 or i % 6 == 0:
        result.append(i)

print("Числа, кратні 4 або 6:")
print(result)
