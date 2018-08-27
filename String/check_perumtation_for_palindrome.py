from collections import defaultdict


def permutation(string):

    odd_chars = set()

    for s in string:
        if s in odd_chars:
            odd_chars.remove(s)
        else:
            odd_chars.add(s)

    return len(odd_chars) <= 1




print(permutation('civic'))