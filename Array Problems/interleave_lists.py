def interleave_lists(ar):
    result = []
    max_length = 0
    for i in ar:
        max_length = max(max_length,len(i))

    for _ in range(max_length):
        for i in ar:
            if len(i) > 0:
                result.append(i.pop(0))
    return result

print(interleave_lists([[1,2,3],[9,0],[5],[-4,-5]]))