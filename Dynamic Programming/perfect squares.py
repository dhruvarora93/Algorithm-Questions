def perfect_squares(n):
    table = [float('inf')] * (n+1)
    table[0] = 0
    for i in range(1, n+1):
        minimum = float('inf')
        j = 1
        while i - j*j >= 0:
            minimum = min(minimum,table[i-j*j]+1)
            j += 1
        table[i] = minimum
    return table[n]

print(perfect_squares(19))