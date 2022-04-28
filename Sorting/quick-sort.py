"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array): #uses this strategy https://www.youtube.com/watch?v=cnzIChso3cc
    if len(array) <= 1:
        return array
    i = 0
    pivot_index = 0
    for item in range(len(array)):
        if array[pivot_index] > array[item]:
            i += 1
            #print(i, array[item], "less than", array[pivot_index])
            array[i], array[item] = array[item], array[i]
    array[i], array[pivot_index] = array[pivot_index], array[i]
    #print(array[:i]+array[i+1:])
    return quicksort(array[:i]) + [array[i]] + quicksort(array[i+1:])

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))