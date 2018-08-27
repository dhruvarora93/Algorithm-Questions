def solution(T):
    unique_candies=set(T)
    if len(unique_candies) >= len(T)/2:
        return int(len(T)/2)
    else:
        return int(len(unique_candies))








T = [1,2,3,4,5,6,7,8]
print(solution(T))