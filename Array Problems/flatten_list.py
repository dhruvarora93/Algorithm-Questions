def flatten_list(ar):
    flattened_list = []
    for i in ar:
        if type(i) == int:
            flattened_list.append(i)
        else:
            j = 0
            while type(i[j]) != int:
                i = i[j]
            for j in i:
                flattened_list.append(j)
            #result = flatten_list(i)
            #flattened_list.extend(result)

    return flattened_list




def flat(ar):
    result = []
    for i in ar:
        if type(i) == int:
            result.append(i)
        else:
            result.extend(flat(i))
    return result

print(flat([1,[4,[6,[3,5]]]]))
