import math


def check_array(ar):

    matches = {0:0,1:1,6:9,8:8,9:6}

    if len(ar) % 2 == 0:
        left = (len(ar) // 2) - 1
        right = left + 1
    else:

        mid = len(ar) // 2
        left = mid - 1
        right = mid + 1

        if ar[mid] not in matches or ar[mid] == 6 or ar[mid] == 9:
            return False

    while left >= 0:

        if ar[left] != matches[ar[right]] or ar[right] != matches[ar[left]]:
            return False

        left -= 1
        right += 1

    return True

print(check_array([1,6,9,1]))