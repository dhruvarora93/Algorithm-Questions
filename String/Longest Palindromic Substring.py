def longest_pallindrome(str):

    n = len(str)
    table = [[0]*n for _ in range(n)]

    i = 0
    while i < n:
        table[i][i] = 1
        i += 1

    max_length = 1
    start = 0
    i = 0
    while i < n-1:
        if str[i] == str[i+1]:
            table[i][i+1] = 1
            start = i
            max_length = 2

        i += 1

    k = 3

    while k <= n:
        i = 0
        while i < (n - k + 1):

            j = i + k - 1

            if table[i+1][j-1] and str[i] == str[j]:
                table[i][j] = 1
                if k > max_length:
                    max_length = k
                    start = i

            i += 1

        k += 1

    return str[start:start+max_length]


print(longest_pallindrome('aaabc'))