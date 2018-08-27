def wiggle_sort(nums):
    nums_copy = list(nums)
    nums_copy.sort()
    start = 0
    end = len(nums_copy) - 1
    i = 0
    while i < len(nums):
        nums[i] = nums_copy[start]
        i += 1
        if i >= len(nums):
            break
        nums[i] = nums_copy[end]
        i += 1
        start += 1
        end -= 1
    return nums


def wiggle1(nums):

    wiggle = False

    for i in range(len(nums)-1):
        if nums[i+1] > nums[i]:
            if wiggle:
                nums[i+1], nums[i] = nums[i], nums[i+1]

        else:
            if not wiggle:
                nums[i + 1], nums[i] = nums[i], nums[i + 1]

        wiggle = not wiggle

    return nums




print(wiggle1([5,4,3,2,1]))