def binary_search(array, element):
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == element:
            return mid
        elif array[mid] < element:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr_input = input("Введіть елементи відсортованого масиву через пробіл: ")
arr = list(map(int, arr_input.split()))

x = int(input("Введіть елемент для пошуку: "))

index = binary_search(arr, x)

if index != -1:
    print(f"Елемент знайдено на індексі {index}")
else:
    print("Елемент не знайдено (-1)")
