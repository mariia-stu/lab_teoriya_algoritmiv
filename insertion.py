def insertion_sort(arr):
    count = 0
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        print(f"Етап {i}: {arr}")
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            count += 1
        arr[j + 1] = key
    print(f"Всього виконано {count} дій")
    return arr


arr = list(map(int, input("Введіть елементи масиву через пробіл: ").split()))

print("Початковий масив:", arr)
sorted_arr = insertion_sort(arr)
print("Відсортований масив:", sorted_arr)

