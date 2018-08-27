def number_exists(numbers, n, target):
    if (n == 0 and target != 0):
        return False

    if (target == 0):
        return True

    if (numbers[n - 1] > target):
        return number_exists(numbers, n - 1, target);

    return number_exists(numbers, n - 1, target) or number_exists(numbers, n - 1, target - numbers[n - 1])


numbers = [1, 6, 5, 4, 7]
print(number_exists(numbers, len(numbers), 3))