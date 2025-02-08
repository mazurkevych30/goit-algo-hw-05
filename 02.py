def binary_search(arr, target):
    left = 0  # Ліва межа масиву
    right = len(arr) - 1  # Права межа масиву
    counter = 0
    upper_bound = None

    while left <= right:
        counter += 1
        mid = (left + right) // 2  # Знаходимо середину масиву

        if arr[mid] == target:
            return (counter, arr[mid])
        elif arr[mid] < target:
            left = mid + 1  # Якщо шуканий елемент більший, зміщуємо ліву межу
        else:
            right = mid - 1  # Якщо шуканий елемент менший, зміщуємо праву межу

    if upper_bound is None and left < len(arr):
        upper_bound = arr[left]

    return (counter, upper_bound)

# Приклад використання
array = [2.4, 5.1, 8.7, 12.9, 16.3, 23.5, 38.8, 56.2, 72.6, 91.4]
numer_target = 38.8
result = binary_search(array, numer_target)

print(result)
