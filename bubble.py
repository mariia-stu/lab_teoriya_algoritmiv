def bubble_sort(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        swapped = False
        print(f"Етап {i+1}: {arr}")
        for j in range(0, n - i - 1):
            count += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    print(f"Всього виконано {count} дій")
    return arr


# Введення даних користувачем
arr = list(map(int, input("Введіть елементи масиву через пробіл: ").split()))

print("Початковий масив:", arr)
sorted_arr = bubble_sort(arr)
print("Відсортований масив:", sorted_arr)

