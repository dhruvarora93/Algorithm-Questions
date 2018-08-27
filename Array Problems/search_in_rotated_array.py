def search(nums,target):
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        ascending = nums[start] <= nums[mid]
        if ascending:
            if nums[start] <= target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if nums[mid] < target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1

    return -1

print(search([5,1,3],3))