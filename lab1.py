import math

x1, y1, z1 = map(int, input("Введіть координати точки A (x1 y1 z1) через пробіл: ").split())
x2, y2, z2 = map(int, input("Введіть координати точки B (x2 y2 z2) через пробіл: ").split())
x3, y3, z3 = map(int, input("Введіть координати точки C (x3 y3 z3) через пробіл: ").split())
x4, y4, z4 = map(int, input("Введіть координати точки D (x4 y4 z4) через пробіл: ").split())

len_AB = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
len_CD = math.sqrt((x4 - x3)**2 + (y4 - y3)**2 + (z4 - z3)**2)

if len_CD == 0:
    print("Помилка: довжина вектора CD дорівнює нулю, відношення не існує.")
else:
    ratio = len_AB / len_CD
    print(f"Відношення довжин векторів AB та CD: {ratio}")
