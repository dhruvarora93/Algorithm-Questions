def lengthOfLongestSubstring(s):
    if len(s) == 0:
        return 0
    count = [0] * len(s)
    count[0] = 1

    for i in range(1, len(s)):
        index = count[i - 1]
        substring = s[i-index:i]
        matched_index = substring.rfind(s[i])
        if matched_index != -1:
            count[i] = index - matched_index
        else:
            count[i] = count[i - 1] + 1

    return max(count)


def longest_substring(s):
    longest, count, seen = 0, 0, {}
    for i in range(len(s)):
        c = s[i]
        if c in seen:
            count = min(i - seen[c], count + 1)
        else:
            count += 1
        seen[c] = i
        longest = max(longest, count)
    return longest


print(longest_substring("abba"))