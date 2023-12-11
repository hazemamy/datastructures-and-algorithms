def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j + 1] < arr[j]:
            tmp = arr[j + 1]
            arr[j + 1] = arr[j]
            arr[j] = tmp
            j -= 1
    return arr



arr1 = [34,555,12,15,35,624]

insertionSort(arr1)

print(arr1)