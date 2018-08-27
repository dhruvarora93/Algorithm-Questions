def partition(ar, start, end):
    pivot = ar[(start + end) // 2]

    while start <= end:
        while ar[start] < pivot:
            start += 1
        while ar[end] > pivot:
            end -= 1
        if start <= end:
            ar[start], ar[end] = ar[end], ar[start]
            start += 1
            end -= 1

    return start


def quick_sort(ar,low,high):
    index = partition(ar,low,high)
    if low < index - 1:
        quick_sort(ar,low,index-1)
    if index < high:
        quick_sort(ar,index,high)
    return ar
print(quick_sort([55,23,26,2,18,78,23,8,2,3],0,9))