def linear_search(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return i
    return -1

arr_input = input("Введіть елементи масиву через пробіл: ")
arr = list(map(int, arr_input.split()))

x = int(input("Введіть елемент для пошуку: "))

index = linear_search(arr, x)

if index != -1:
    print(f"Елемент знайдено на індексі {index}")
else:
    print("Елемент не знайдено (-1)")
