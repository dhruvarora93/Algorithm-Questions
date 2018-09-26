def longest_subarray_with_k_odd(array, k):
    start, end, count = 0, 0, 0
    starting, ending = 0,0
    longest_length = float('-inf')
    while end < len(array):
        if array[end] % 2 != 0:
            count += 1
        while count > k and start < end:
            ele = array[start]
            if ele % 2 != 0:
                count -= 1
            start += 1
        last = longest_length
        longest_length = max(longest_length, end - start + 1)
        if last != longest_length:
            starting = start
            ending = end
        end += 1
    if count != k:
        print([])
    else:
        print(array[starting:ending+1])


longest_subarray_with_k_odd([12, 5, 16, 10, 3, 4, 6, 7], 1)