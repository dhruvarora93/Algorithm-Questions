def number_exists(numbers, n, target):
    if (n == 0 and target != 0):
        return False

    if (target == 0):
        return True

    if (numbers[n - 1] > target):
        return number_exists(numbers, n - 1, target);

    return number_exists(numbers, n - 1, target) or number_exists(numbers, n - 1, target - numbers[n - 1])


numbers = [1, 6, 5, 4, 7]
#print(number_exists(numbers, len(numbers), 2))


def number_exists_dp(numbers, n, target):
    table = [[False for _ in range(target+1)] for _ in range(n+1)]

    for i in range(n+1):
        table[i][0] = True

    for j in range(1,target+1):
        table[0][j] = False

    for i in range(1,n+1):
        for j in range(1,target+1):
            if j < numbers[i-1]:
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = table[i-1][j] or table[i-1][j-numbers[i-1]]
    return table[n][target]


print(number_exists_dp(numbers, len(numbers), 12))


