def sum_of_binary(a,b):
    i = len(a) - 1
    j = len(b) - 1
    result = []
    sum = 0
    while i >= 0 or j >= 0 or sum == 1:
        char_at_i = a[i] if i >= 0 else '0'
        char_at_j = b[j] if j >= 0 else '0'
        sum += int(char_at_i) + int(char_at_j)
        result.append(str(int(sum % 2)))
        sum = sum // 2
        i -= 1
        j -= 1
    return ''.join(result[::-1])


print(sum_of_binary('1110','1110'))




