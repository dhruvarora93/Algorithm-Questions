import random


def get_random(floor, ceiling):
    return random.randint(floor, ceiling)


def naive_shuffle(the_list):
    # For each index in the list
    for first_index in range(0, len(the_list)):
        # Grab a random other index
        second_index = get_random(first_index, len(the_list) - 1)
        # And swap the values
        if second_index != first_index:
            the_list[first_index], the_list[second_index] = \
                the_list[second_index], the_list[first_index]

    return the_list


print(naive_shuffle([1,2,3]))


