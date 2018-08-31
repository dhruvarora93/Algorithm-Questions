def combinationSum(candidates, target):

    result = []
    final = []
    helper(final,result,candidates,target,0)
    print(final)


def helper(output, temp, candidates, target, index):

    if target < 0:
        return
    elif target == 0:
        output.append(list(temp))
    else:
        for i in range(index,len(candidates)):
            temp.append(candidates[i])
            helper(output,temp,candidates,target-candidates[i],i)
            temp.pop()


combinationSum([2,3,6,7],8)