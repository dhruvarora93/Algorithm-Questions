import math


def closest_palindrome(string):
    num = int(string)

    if string == '0':
        return '1'
    if string == '11':
        return '9'
    if string <= '10' or math.log10(num) % 1 == 0:
        return str(num - 1)

    exp = len(string) // 2
    offset = pow(10, exp)

    minimum = min_from_target(num, palindrome(num), palindrome(num+offset), palindrome(num-offset))

    return minimum


def min_from_target(num, param, param1, param2):
    array = [param, param1, param2]
    min_distance = float('inf')
    minimum = None
    for i in array:
        if i != num and abs(i - num) < min_distance:
            min_distance = abs(i - num)
            minimum = i
        elif i != num and abs(i - num) == min_distance and i < minimum:
            minimum = i
    return str(minimum)


def palindrome(number):
    num = [i for i in str(number)]
    start = 0
    end = len(num) - 1
    while start < end:
        num[end] = num[start]
        start += 1
        end -= 1

    return int(''.join(num))


print(closest_palindrome('1456'))
