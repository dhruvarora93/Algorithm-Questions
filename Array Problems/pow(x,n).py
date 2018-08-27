def power(x,n):
    if n < 0:
        n = -n
        x = 1 / x

    answer = 1
    while n:
        if n % 2 == 1:
            answer *= x
        x *= x
        n = n // 2

    return answer


print(power(2,5))