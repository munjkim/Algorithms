def bubbleSort(A) -> list:
    for i in range(len(A) - 1, 0, -1):
        for j in range(0, i):
            print(i, j)
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A

arr = [5, 4, 3, 2, 1]
print(bubbleSort(arr))

