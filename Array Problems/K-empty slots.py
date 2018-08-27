def check_for_slots(days, left, right, k):
    for i in range(left+1, right):
        if days[i] < days[left] or days[i] < days[right]:
            return [i, i + k + 1]
    return None


def kEmptySlots(flowers, k, m):
        days = [0] * len(flowers)
        for day, position in enumerate(flowers, 1):
            days[position - 1] = day
        ans = float('-inf')
        left, right = 0, k - 1
        while right < len(days):
            slot = check_for_slots(days, left, right, k)
            if slot is not None:
                left, right = slot[0], slot[1]
            else:
                ans = max(ans, max(days[left], days[right]))
                left, right = right, right + k + 1

        return ans if ans > float('-inf') else -1


print(kEmptySlots([1,2,7,6,4,3,5],2,2))


def solution(A, K, M):
    days = [0] * len(A)
    for day, position in enumerate(A, 1):
        days[position - 1] = day
    print(days)

print(solution([1,4,3,2,5],1,1))



