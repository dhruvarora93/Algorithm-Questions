def trapping_water(array):
    if not array:
        return 0

    left_max = [0]*len(array)
    right_max = [0]*len(array)

    left_max[0] = 0
    right_max[len(array) - 1] = 0
    answer = 0
    for i in range(1,len(array)):
        left_max[i] = max(left_max[i-1], array[i])

    for i in range(len(array)-2, -1, -1):
        right_max[i] = max(right_max[i+1], array[i])

    for i in range(1,len(array)-1):
        answer += min(left_max[i], right_max[i]) - array[i]

    print(answer)


def trapping_water_using_stack(array):
    ans, current = 0, 0
    stack = []
    while current < len(array):
        while stack and array[current] > array[stack[-1]]:
            top = stack.pop()
            if not stack:
                break
            distance = current - stack[-1] - 1
            area = min(array[current], array[stack[-1]]) - array[top]
            ans += distance * area

        stack.append(current)
        current += 1

    print(ans)



heights = [0,1,0,2,1,0,1,3,2,1,2,1]
trapping_water_using_stack(heights)