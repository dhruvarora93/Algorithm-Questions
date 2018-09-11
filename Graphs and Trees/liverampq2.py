def solution(A):
    # write your code in Python 3.6

    unique_vacations=list(set(A))
    count_of_vacations={}
    for vacation in unique_vacations:
        if vacation in count_of_vacations:
            count_of_vacations[vacation] += 1
        else:
            count_of_vacations[vacation] = 1
    left=0
    min_length=len(A)+1
    count=0
    for right in range(len(A)):
        if A[right] in count_of_vacations:
            count_of_vacations[A[right]] -= 1
            if count_of_vacations[A[right]] >= 0:
                count += 1
            while count == len(unique_vacations):
                if right - left + 1 < min_length:
                    min_length = right-left+1
                if A[left] in count_of_vacations:
                    count_of_vacations[A[left]] += 1
                    if count_of_vacations[A[left]] > 0:
                        count -= 1
                left += 1





    if min_length > len(A):
        return 0

    return min_length


#print(solution([2,1,1,3,2,1,1,3]))


def contains_sequence(seq):
    start = end = 0
    unique_vacations = set(seq)
    sequence = []
    minimum_length = float('inf')
    while end < len(seq):
        sequence.append(seq[end])
        end += 1

        while unique_vacations == set(sequence) and start <= end:
            index = end - start
            minimum_length = min(minimum_length, index)
            sequence.remove(seq[start])
            start += 1

    return minimum_length

print(contains_sequence([2,1,1,3,3,3,3,1,1,3]))




def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    query = set(t)
    start = end = 0
    sequence = []
    result = ""
    minimum_length = float('inf')
    while end < len(s):
        sequence.append(s[end])
        end += 1

        while query.issubset(set(sequence)) and start <= end:
            index = end - start
            old_min = minimum_length
            minimum_length = min(minimum_length, index)
            if old_min != minimum_length:
               result = s[start:end]
            sequence.remove(s[start])
            start += 1

    return result


print(minWindow("ADOBECODEBANC","ABC"))