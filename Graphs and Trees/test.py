def previous_time(S):
    time = set(S)
    hour = int(S[0:2])
    minute = int(S[3:5])
    while True:
        minute -= 1
        if minute == -1:
            minute = 59
            hour = 23 if hour == 0 else hour - 1

        new_time = "%02d:%02d" % (hour, minute)
        if set(new_time) <= time:
            return new_time
    return new_time



print(previous_time("00:59"))

def nextClosestTime(time):
    s = set(time)

    hour = int(time[0:2])
    minute = int(time[3:5])
    while True:
        minute += 1
        if minute == 60:
            minute = 0
            hour = 0 if hour == 23 else hour + 1

        time = "%02d:%02d" % (hour, minute)
        if set(time) <= s:
            return time
    return time


#print(nextClosestTime('12:57'))

import math
def numSquares(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 0:
        return 0
    square_root = math.floor(math.sqrt(n))
    if square_root == 1:
        return n
    minimum_numbers = float('inf')
    minimum_numbers_required = {}
    minimum_numbers_required[0] = 0
    minimum_numbers_required[1] = 1
    minimum_numbers_required[2] = 2
    minimum_numbers_required[3] = 3
    for i in range(1,square_root+1):
        if n - (i * i) not in minimum_numbers_required:
            minimum_numbers_required[n - (i * i)] = numSquares(n - (i * i))
        number_count = 1 + minimum_numbers_required[n - (i * i)]
        minimum_numbers = min(minimum_numbers, number_count)

    return minimum_numbers


#print(numSquares(42))