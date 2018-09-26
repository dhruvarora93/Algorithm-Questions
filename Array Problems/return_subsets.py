def get_subsets(l):
    allsubsets = []
    index = len(l)
    if index == 0:
        allsubsets.append([])
    else:
        item = l.pop()
        allsubsets = get_subsets(l)
        more_subsets=[]
        for i in allsubsets:
            new_Subset=[]
            new_Subset.extend(i)
            new_Subset.append(item)
            more_subsets.append(new_Subset)
        allsubsets.extend(more_subsets)

    return allsubsets


print(get_subsets([1,2,3,4]))



