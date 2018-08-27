def count_steps(n,memo):
    if n<0:
        return 0
    elif n==0:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n]=count_steps(n-1,memo)+count_steps(n-2,memo)+count_steps(n-3,memo)
        return memo[n]



memo={}
print(count_steps(10,memo))