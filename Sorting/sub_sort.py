def find_unsorted_seq(numbers):

    left_index = find_left_increasing(numbers)

    if left_index == len(numbers) - 1:
        return 0

    right_index = find_right_increasing(numbers)

    left_min = right_index
    right_max = left_index

    for i in range(left_index + 1,right_index):

        if numbers[i] < numbers[left_min]:
            left_min = i

        if numbers[i] > numbers[right_max]:
            right_max = i

    start = shrink_left(numbers,left_min,left_index)
    end = shrink_right(numbers,right_max,right_index)

    print(str(start) + ',' + str(end))


def find_left_increasing(numbers):

    for i in range(1,len(numbers)):
        if numbers[i] < numbers[i-1]:
            return i -1

    return len(numbers) - 1


def find_right_increasing(numbers):

    for i in range(len(numbers)-2,-1,-1):
        if numbers[i] > numbers[i+1]:
            return i + 1


def shrink_left(numbers,min_index,ending):
    min_number = numbers[min_index]
    for i in range(ending + 1):
        if numbers[i] >= min_number:
            return i


def shrink_right(numbers,max_index,starting):
    max_number = numbers[max_index]
    for i in range(starting,len(numbers)):
        if numbers[i] >= max_number:
            return i - 1


find_unsorted_seq([1,2,4,7,10,11,8,12,5,6,16,18,19])