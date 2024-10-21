def findDuplicate(arr):
    # Write your code here
    length = len(arr)
    for i in range(length):
        if arr[i] == arr[length-1 - i]:
            return arr[i]
            break

print(findDuplicate([3,4,5,6,7,3,4,6,7]))