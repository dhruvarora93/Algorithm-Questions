def remove_duplicates(ar):
    n = len(ar)

    if n == 0 or n == 1:
        return n
    j = 0
    count = 1
    for i in range(1,n):
        if count < 2 or ar[i] != ar[i-2]:
            ar[j+1] = ar[i]
            j += 1
            count += 1
    print(ar)
    return j+1


print(remove_duplicates([1,1,1,1,2,2,3,3,3,3,3,4,5,6]))