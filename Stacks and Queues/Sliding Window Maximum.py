from collections import deque


def sliding_window_max(nums,k):

    output = []
    queue = deque()

    for end in range(len(nums)):

        while queue and nums[end] > queue[-1]:
            queue.pop()

        queue.append(nums[end])

        start = end - k + 1

        if start < 0:
            continue

        output.append(queue[0])

        if nums[start] == queue[0]:
            queue.popleft()

    return output

print(sliding_window_max([1,3,-1,3,5,3,6,7],3))