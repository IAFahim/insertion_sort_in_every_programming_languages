def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        print("loop: " + str(i) + "\t\t\t\t" + str(arr[0:i]) + " + [" + str(arr[i]) + "]")
        j = i - 1
        while j >= 0 and key < arr[j]:
            if j!=0:
                print("\tinner loop: " + str(j) + "\t" + str(arr[0:j + 1]) + (
                        " swapping " + str(arr[j - 1]) + " and " + str(
                    arr[j])) + " => Current State: " + str(arr[0:i]))
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
        print(
            "placed [" + str(arr[j + 1]) + "] at index: " + str(j + 1) + "\t=> Current State: " + str(
                arr[0:i + 1]) + "\n")
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


arr = [4, 2, 0, 6, 9]

ascending = insertion_sort(arr)
print(ascending)

descending = insertion_sort_reverse(arr)
print(descending)
