def setWay(arr):
    ar = set(arr)
    for i in range(0, len(arr)):
        for j in range(i, len(arr)):
            number = -1 * (arr[i] + arr[j])
            if ar.contains(number):  # does number exists in the array?
                print(arr[i], arr[j], number)


# assuming reptition
def bsWay(arr):
    sort(arr)
    for i in range(0, len(arr)):
        for j in range(i, len(arr)):
            number = -1 * (arr[i] + arr[j])
            if binary_search(arr, number):
                print(arr[i], arr[j], number