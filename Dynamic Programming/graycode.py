def grayCode(n):
    dp = [0]
    for i in range(n):
        dp.extend([x | (1 << i) for x in dp[::-1]])
    return dp

print(grayCode(4))