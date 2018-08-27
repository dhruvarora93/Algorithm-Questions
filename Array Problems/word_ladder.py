from collections import deque


def word_ladder(begin,end,word_list):
    if end not in word_list:
        return 0
    count = 0
    queue = deque()
    queue.insert(0,begin)
    visited = [None]*len(wordList)
    remain = 1
    total = 0
    visited.append(begin)
    while queue:
        word = queue.popleft()
        remain -= 1
        if word == end:
            return count + 1

        for w in word_list:
            if onediff(word, w) == 1 and w not in visited:
                total += 1
                visited.append(w)
                queue.append(w)

        if total > 0 and remain == 0:
            count += 1
            remain = total
            total = 0


def onediff(w1,w2):
    count = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            count += 1
    return count

beginWord = "hot"
endWord = "dog"
wordList = ["hot","cog","dog","tot","hog","hop","pot","dot"]
print(word_ladder(beginWord,endWord,wordList))


"hot"
"dog"
["hot","cog","dog","tot","hog","hop","pot","dot"]
a = "lost"
b = "miss"

["most","mist","miss","lost","fist","fish"]