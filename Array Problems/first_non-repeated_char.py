
def first_non_repeating_character(ar):
    count = {}
    for i,j in enumerate(ar):
        count[j] = i

    for i,j in enumerate(ar):
        if count[j] == i:
            return j
        else:
            count[j] = -1


    return None




print(first_non_repeating_character(['b','b','b','c','d']))



def first_non_repeating_character1(ar):

    count = {}
    for i,j in enumerate(ar):
        if j not in count:
            count[j] = (i,1)
        else:
            count[j] = (i,-1)
    indices = []
    for i, j in count.items():

        if j[1] == 1:
            indices.append(j[0])

    if not indices:
        return None
    return ar[min(indices)]




print(first_non_repeating_character(['b','b','b','c']))