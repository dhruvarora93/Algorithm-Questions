def min_product(a,b):
    bigger = max(a,b)
    smaller = min(a,b)

    return min_product_helper(smaller, bigger)


def min_product_helper(smaller,bigger):
    if smaller == 0:
        return 0
    elif smaller == 1:
        return bigger

    s = smaller // 2
    side1 = min_product_helper(s,bigger)
    side2 = side1
    if smaller % 2 == 1:
        side2 = min_product_helper(smaller-s,bigger)

    return side1 + side2


print(min_product(8,8))