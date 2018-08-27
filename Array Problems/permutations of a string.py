def get_permutation(string):

    if len(string) <= 1:
        return set(string)

    last_char_removed_string = string[:-1]
    last_char = string[-1]

    all_permutations = get_permutation(last_char_removed_string)
    permutations = set()

    for i in all_permutations:

        for j in range(len(last_char_removed_string)+1):
            permutation = i[:j]+last_char+i[j:]
            permutations.add(permutation)

    return permutations


print(get_permutation('abc'))

print([1,2,3] + [2])

