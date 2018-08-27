def decode_ways(string):
    n = len(string)
    table = [0] * (n + 1)
    table[0] = 1
    table[1] = 1
    for i in range(2,n+1):
        if string[i-1] == 0 and (string[i-2] > '2' or string[i-2] == '0'):
            return 0
        elif string[i-1] == 0:
            table[i] += table[i-2]
        elif (string[i-2] == '1') or (string[i-2] == '2' and string[i-1] > '0' and string[i-1] <= '6'):
            table[i] += table[i-1] + table[i-2]
        else:
            table[i] += table[i-1]

    return table[n]


print(decode_ways('237'))