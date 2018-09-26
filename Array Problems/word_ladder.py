from collections import deque
from string import ascii_lowercase
from collections import defaultdict

def ladder_length(begin, end, word_list):

    queue = set([begin])
    output_words = defaultdict(list)
    word_list = set(word_list)
    while queue:
        nxt = set()
        for item in queue:

            for word in generate_neighbors(item, word_list):
                if word in output_words or word in queue:
                    continue
                else:
                    output_words[item].append(word)
                    nxt.add(word)
        queue = nxt
        if end in queue:
            res = []
            dfs([begin], begin, res, output_words, end)
            return res
    return []


def generate_neighbors(word, word_list):
    for i in range(len(word)):
        for letter in ascii_lowercase:
            candidate = word[:i] + letter + word[i+1:]
            if candidate in word_list:
                yield candidate


def dfs(sofar, cur, res, graph,end):
        if cur == end:
            res.append(sofar)
            return
        for neigh in graph[cur]:
            dfs(sofar + [neigh], neigh, res, graph,end)


beginWord = "red"
endWord = "tax"
wordList = ["ted","tex","red","tax","tad","den","rex","pee"]
print(ladder_length(beginWord,endWord,wordList))


