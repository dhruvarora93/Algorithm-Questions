def balance_parens(string):
    keep = [False] * len(string)

    for idx,letter in enumerate(string):
        if letter == '(':
            for j in range(idx+1,len(string)):
                if not keep[j] and string[j] == ')':
                    keep[idx] = True
                    keep[j] = True
                    break


    result = ""
    for idx in range(len(string)):
        if keep[idx] or (string[idx] != '(' and string[idx] != ')'):
            result += string[idx]

    return result


def balance_parantheses1(string):

    s = list(string)
    count = 0

    for idx, char in enumerate(s):
        if char == '(':
            count += 1
        elif char == ')':
            if count == 0:
                s[idx] = '#'
            else:
                count -= 1

    for idx in range(len(s)-1,-1,-1):
        if count == 0:
            break

        if s[idx] == '(':
            s[idx] = '#'
            count -= 1

    return ''.join(s).replace('#','')




print(balance_parantheses1("()())()(("))