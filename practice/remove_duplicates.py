def remove_duplicates(nums):
    j = 0
    first = nums[0]
    for i in range(1,len(nums)):
        if nums[i] != first:
            j = j + 1
            nums[j] = nums[i]
            first = nums[i]
    return j+1


print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]))

