def max_product(nums,k):
    if k <= 1: return 0
    prod = 1
    ans = left = 0
    for right, val in enumerate(nums):
        prod *= val
        while prod >= k:
            prod /= nums[left]
            left += 1

        ans += right - left + 1
    return ans



ar = [1,2,3,2,10]

print(max_product(ar,20))
