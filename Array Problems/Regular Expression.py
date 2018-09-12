def isMatch(s, p):

    table = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]

    table[0][0] = True

    for i in range(1, len(table[0])):
        if p[i-1] == '*':
            table[0][i] = table[0][i-2]

    for i in range(1,len(table)):
        for j in range(1,len(table[0])):
            if p[j-1] == s[i-1] or p[j-1] == '.':
                table[i][j] = table[i-1][j-1]
            elif p[j-1] == '*':
                table[i][j] = table[i][j-2]
                if s[i-1] == p[j-2] or p[j-2] == '.':
                    table[i][j] = table[i][j] or table[i-1][j]
            else:
                table[i][j] = False
    return table[-1][-1]


print(isMatch('aab','c*a*b*'))