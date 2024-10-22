def bubbleSort(arr, n):
    # code here
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


n = 5
arr = [4, 1, 3, 9, 7]

print(bubbleSort(arr, n))