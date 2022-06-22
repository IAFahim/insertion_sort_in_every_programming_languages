def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
    return arr


def insertion_sort_reverse(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
    return arr


import random
arr = random.sample(range(100), random.randint(1, 50))

ascending = insertion_sort(arr)
print(ascending)

descending = insertion_sort_reverse(arr)
print(descending)
