def sum_exists(numbers, target):
    start, end, sum = 0, 0, 0

    while end < len(numbers):
        sum += numbers[end]
        end += 1

        while sum >= target and start <= end:
            if sum == target:
                return True
            sum -= numbers[start]
            start += 1
    return False

#print(sum_exists([1,4,6,21],21))
from collections import defaultdict
a = defaultdict(list)
a['dh'] += [3]
print(a)
