def merge(left,right):

    mered_list_size = len(left) + len(right)
    merged_list = [None] * mered_list_size

    left_index, right_index, merge_index = 0, 0, 0

    while merge_index < mered_list_size:
        isleft = left_index < len(left)
        isright = right_index < len(right)

        if isleft and (not isright or left[left_index] < right[right_index]):
            merged_list[merge_index] = left[left_index]
            left_index += 1

        else:
            merged_list[merge_index] = right[right_index]
            right_index += 1

        merge_index += 1

    return merged_list


def merge_sort(ar):
    if len(ar) <= 1:
        return ar
    mid = len(ar) // 2
    start = merge_sort(ar[:mid])
    end = merge_sort(ar[mid:])

    return list(merge(start,end))


print(merge_sort([10,9,8,5,0]))