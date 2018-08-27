def insertion_sort(ar):

    for i in range(1,len(ar)):

        j = i-1
        key = ar[i]

        while j >= 0 and ar[j] > key:
            ar[j+1] = ar[j]
            j -= 1

        ar[j+1] = key

    return ar


print(insertion_sort([55,23,26,2,18,78,23,8,2,3]))

