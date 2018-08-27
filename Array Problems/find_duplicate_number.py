def find_duplicate(nums):
    if len(nums) > 0:
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        head = 0
        while slow != head:
            slow = nums[slow]
            head = nums[head]

        return slow

print(find_duplicate([1,3,2,3,4]))