def reverse_words(ar):

    ar.reverse()

    number_of_words = 1
    indices = []
    for i,j in enumerate(ar):
        if j == ' ':
            number_of_words += 1
            indices.append(i)

    indices.append(len(ar))
    count = 0
    starting_index = 0

    while count < number_of_words:
        last_index = indices[count] - 1
        while starting_index < last_index:
            temp = ar[starting_index]
            ar[starting_index] = ar[last_index]
            ar[last_index] = temp
            starting_index += 1
            last_index -= 1

        starting_index = indices[count] + 1
        count += 1


    print(''.join(ar))




reverse_words(['c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ])