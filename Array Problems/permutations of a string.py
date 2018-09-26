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


def compress(data):
    seen = set()
    output = []
    index = 0
    while index < len(data):
        if data[index] not in seen:
            output.append((0, data[index]))
            seen.add(data[index])
            for i in range(index + 1):
                seen.add(data[i:index + 1])
            index += 1
        else:
            matched_length = 1
            for i in range(index, len(data)):
                if data[index:i+1] in seen:
                    matched_length = max(matched_length, len(data[index:i+1]))
            output.append((1, matched_length, matched_length))
            for i in range(index+1):
                seen.add(data[i:index+1])
            index += matched_length
    print(output)


compress('FOOFOODFOOD')
