def fast_sort(ar,range1):

    range_matrix = [0] * (range1+1)
    result = []
    for i in ar:
        range_matrix[i] += 1

    for index,value in enumerate(range_matrix[::-1]):
        if value != 0:
            for _ in range(value):
                result.append(index)

    return result



print(fast_sort([37,89,41,65,91,53],100))

# Time, Space Complexity = O(range)

