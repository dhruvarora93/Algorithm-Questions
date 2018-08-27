def myAtoi(nums):
    first_char = None
    index = None
    for i in range(len(nums)):
        if nums[i] != ' ':
            first_char = nums[i]
            index = i
            break
    result = ''
    a = [str(i) for i in range(0,10)]
    if first_char == '-' or first_char in a:
        result += first_char
        index += 1
        while  index < len(nums) and nums[index] in a:
            result += nums[index]
            index += 1
    else:
        result = '0'
    if int(result) > pow(2,31):
        result = 2147483648
    elif int(result) < pow(-2,31):
        result = -2147483648
    print(int(result))


myAtoi("words and 987")



