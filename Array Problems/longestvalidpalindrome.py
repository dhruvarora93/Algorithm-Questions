def longest_valid_parantheses(string):
    stack = [-1]
    maxlen = 0

    for i, c in enumerate(string):
        if c == '(':
            stack.append(i)
        else:
            stack.pop()
            if stack:
                maxlen = max(maxlen, i-stack[-1])
            else:
                stack.append(i)
    return maxlen


print(longest_valid_parantheses('(((()'))