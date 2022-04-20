import math

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
print(indexOf2(listB, 50))