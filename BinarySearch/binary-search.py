"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    head = 0
    tail = len(input_array) -1
    pos = -1
    while head <= tail:
        mid = (head + tail) // 2
        if input_array[mid] == value:
            pos = mid
            break
        else:
            if input_array[mid] < value:
                head = mid +1
            else:
                tail = mid -1
    return pos

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))


"""First Try"""
"""import math

def indexOf(arr, value):
    not_finded = True
    while not_finded:
        arr_length = len(arr)
        print(arr[math.floor(arr_length / 2) - 1], arr[math.floor(arr_length // 2)])
        #print(arr[math.floor(arr_length / 2) - 1] < value)
        #print(arr[math.floor(arr_length / 2) - 1], value)
        if arr_length == 0:
            print('not found')
            not_finded = False
        elif arr_length == 1:
            if arr[0] == value:
                print('founded')
            else:
                print('not founded')
            not_finded = False
        elif arr[math.floor(arr_length / 2) - 1] == value:
            print('founded in mid')
            not_finded = False
        elif arr[math.floor(arr_length / 2) - 1] < value:
            arr = arr[math.floor(arr_length / 2):]
            print(arr)
            #print("end", arr)
        elif arr[math.floor(arr_length / 2) - 1] > value:
            arr = arr[0:math.floor(arr_length / 2)]
            print(arr)
            #print("start", arr)
        else:
            #print('value is here')
            not_finded = False


def indexOf2(arr, value):
    pos = -1
    head = 0
    tail = len(arr) - 1

    while head <= tail:
        mid = (head + tail) // 2
        if arr[mid] == value:
            pos = mid
            break
        else:
            if arr[mid] < value:
                head = mid + 1
            else:
                tail = mid - 1

    return pos

listB = [1, 2, 3, 4, 5, 6]

#print(listB.index(5))
#print(len(listB))
print(listB.index(4))
print(indexOf2(listB, 50))"""