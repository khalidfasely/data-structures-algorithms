def mergeSort(arr):
    if len(arr) < 2:
        return arr

    arrCenter = len(arr) // 2
    a = mergeSort(arr[:arrCenter])
    b = mergeSort(arr[arrCenter:])

    return [    a, b]

unsortedArray = [5, 4, 3, 0, 1]
# result should be [0, 1, 3, 4, 5]
print(mergeSort(unsortedArray))