def helper1(s, t):
    s1 = 0
    t1 = 0
    count = 0
    while s1 < len(s):
        if s[s1] != t[t1]:
            count += 1
        s1 += 1
        t1 += 1

    return count <= 1


def helper2(shorter, longer):
    s1 = 0
    s2 = 0
    count = 0
    while s1 < len(shorter):

        if shorter[s1] != longer[s2]:
            count += 1
            s1 -= 1
        if count > 1:
            return False
        s1 += 1
        s2 += 1

    if count == 0 and s1 == len(shorter):
        return True

    return count == 1


def isOneEditDistance(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    diff = abs(len(s) - len(t))

    if diff > 1:
        return False
    if diff == 0:
        return helper1(s, t)
    else:
        if len(s) > len(t):
            return helper2(t, s)
        else:
            return helper2(s, t)

print(isOneEditDistance("ABDC","ABC"))