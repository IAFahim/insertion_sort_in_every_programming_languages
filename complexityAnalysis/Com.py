# c1 assigment op
# c2 comparison op
# c3 addition/subtraction op
# c4 increment op

def insertion_sort(arr):
    for i in range(1, len(arr)):        # c1 + n(c2) + (n-1)(c4)
        key = arr[i]                    # n(c1)
        j = i - 1                       # n(c3)
        while j >= 0 and key < arr[j]:  # n(2.c2)(n + 1)
            arr[j + 1] = arr[j]         # n*n(c1 + c3)
            j = j - 1                   # n*n(c4)
        arr[j + 1] = key                # n*n(c3 + c1)
    return arr
# c1 + n(c2) + (n-1)(c4) + n(c1) + n(c3) + n(2.c2)(n + 1) + n*n(c1 + c3) + n*n(c4) + n*n(c3 + c1)
# c1+c4 + n.(c1+c2+c3+c4) + n(2.c2)(n + 1) + n*n(2.c1+2.c3+c4)
# O(n^2)