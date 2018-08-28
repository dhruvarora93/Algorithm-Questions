from collections import deque
from string import ascii_lowercase


def ladder_length(begin, end, word_list):

    queue = deque([[begin,1]])
    visited = set([begin])

    while queue:

        item = queue.popleft()
        for word in generate_neighbors(item[0], word_list):
            if word == end:
                return item[1] + 1
            elif word in visited:
                continue
            else:
                visited.add(word)
                queue.append([word,item[1]+1])
    return 0


def generate_neighbors(word,word_list):
    for i in range(len(word)):
        for letter in ascii_lowercase:
            candidate = word[:i] + letter + word[i+1:]
            if candidate in word_list:
                yield candidate


beginWord = "hot"
endWord = "dog"
wordList = ["hot","cot","cog","dog"]
print(ladder_length(beginWord,endWord,wordList))


"hot"
"dog"
["hot","cog","dog","tot","hog","hop","pot","dot"]
a = "lost"
b = "miss"

["most","mist","miss","lost","fist","fish"]