def check_parantheses(num):

    if num == 1:
        return set(['()'])

    else:
        ar = check_parantheses(num-1)
        result = []
        for a in ar:
            for i in range(len(a)):
                result.append(a[:i] + '()' + a[i:])
        return set(result)



print(check_parantheses(3))

