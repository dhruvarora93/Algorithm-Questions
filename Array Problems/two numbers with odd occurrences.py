def print_two_odd(ar,size):
    xor2 = ar[0]
    x = 0
    y = 0
    for i in range(1,len(ar),1):
        xor2 = xor2^ar[i]
    set_bit = xor2 & -xor2

    for i in range(len(ar)):
        if ar[i] & set_bit:
            x = x^ar[i]
        else:
            y = y^ar[i]

    return [x,y]

ar=[1,1,3,3,4,4,5,9]
print(print_two_odd(ar,len(ar)))

a = 1^3
#print(a & a)

from operator import xor
from functools import reduce

def find_odd(array):  # given an array with one element of odd occurence
    # return that element
    return reduce(xor, array)


def find_odds(array):  # given an array with two elements of odd occurence
    # return a pair (a, b) of those two elements
    total_xor = reduce(xor, array)
    mask = total_xor & -total_xor  # mask is least significant bit of a ^ b
    # exactly one of a, b has the corresponding bit set
    part_a = list(filter(lambda a: a & mask == mask, array))
    part_b = list(filter(lambda b: b & mask == 0, array))
    # now we have reduced the problem to where only one element has odd occurence
    print(part_a,part_b)
    a = find_odd(part_a)
    b = find_odd(part_b)
    return (a, b)



#print(print_two_odd(ar))