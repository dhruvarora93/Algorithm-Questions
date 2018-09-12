def find_next_greatest(number):
    digits = []
    for d in str(number):
        digits.append(d)
    if len(digits) <= 1:
        return

    end_index = len(digits) - 1

    while end_index >= 1 and digits[end_index] <= digits[end_index - 1]:
        end_index -= 1
    if end_index != 0:
        found_index = end_index - 1
        for j in range(len(digits)-1,found_index,-1):
            if digits[j] > digits[found_index]:
                digits[found_index] , digits[j] = digits[j], digits[found_index]
                break

    else:
        return 'Next number not possible'

    return ''.join(reverse(digits,end_index))


def reverse(number,index):
    start = index
    end = len(number) - 1
    while start < end:
        number[start], number[end] = number[end], number[start]
        start += 1
        end -= 1
    return number


print(find_next_greatest(1993))




