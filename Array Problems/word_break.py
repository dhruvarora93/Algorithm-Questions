def word_break(s, wordDict):
    start = 0
    stack = [start]
    visited = set()
    while stack:
        start = stack.pop()
        if start in visited:
            continue
        visited.add(start)
        for word in wordDict:
            if s[start:].startswith(word):
                x = len(word)
                if x == len(s[start:]):
                    return True
                stack.append(start + x)
    return False

s = "leetcode"
wordDict = ["leet", "code"]
print(word_break(s,wordDict))


b = 'a'
print(b[2:])