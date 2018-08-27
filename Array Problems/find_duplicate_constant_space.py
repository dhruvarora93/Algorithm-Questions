def find_duplicate(list_of_numbers):
    starting_index = 0
    ending_index = len(list_of_numbers) - 1
    while starting_index < ending_index:

        mid = (starting_index+ending_index)//2
        lower_starting, lower_ending = starting_index, mid
        upper_starting, upper_ending = mid + 1, ending_index

        items_in_lower = 0

        for num in list_of_numbers:
            if num >= lower_starting and num <= lower_ending:
                items_in_lower += 1

        distinct_numbers = lower_ending - lower_starting + 1

        if items_in_lower > distinct_numbers:

            starting_index, ending_index = lower_starting, lower_ending

        else:

            starting_index, ending_index = upper_starting, upper_ending

    return list_of_numbers[starting_index]


print(find_duplicate([3,1,4,2,3]))

