def findMedianSortedArrays( A, B):
    l = len(A) + len(B)
    if l % 2 == 1:
        return kth(A, B, l // 2)
    else:
        return (kth(A, B, l // 2) + kth(A, B, l // 2 - 1)) / 2.0


def kth(a, b, k):
    if not a:
        return b[k]
    if not b:
        return a[k]
    ia, ib = len(a) // 2, len(b) // 2
    ma, mb = a[ia], b[ib]

    # when k is bigger than the sum of a and b's median indices
    if ia + ib < k:
        # if a's median is bigger than b's, b's first half doesn't include k
        if ma > mb:
            return kth(a, b[ib + 1:], k - ib - 1)
        else:
            return kth(a[ia + 1:], b, k - ia - 1)
    # when k is smaller than the sum of a and b's indices
    else:
        # if a's median is bigger than b's, a's second half doesn't include k
        if ma > mb:
            return kth(a[:ia], b, k)
        else:
            return kth(a, b[:ib], k)

print(findMedianSortedArrays([4,5,6,7],[2,3]))

#Time Complexity: O(log m + log n)