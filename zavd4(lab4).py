
numbers = []

while True:
    try:
        a = int(input("Введіть число (0 — завершити): "))
        if a == 0:
            break
        numbers.append(a)
    except ValueError:
        print("Помилка! Введіть лише ціле число.")

if len(numbers) == 0:
    print("Не введено жодного числа.")
else:
    avg = sum(numbers) / len(numbers)
    total = 0
    for num in numbers:
        if num % 2 == 0 and num < avg:
            total += num

    print("Сума парних чисел, менших за середнє:", total)


