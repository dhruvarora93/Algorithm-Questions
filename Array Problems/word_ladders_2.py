import collections
def findLadders(beginWord, endWord, wordList):
    def bfs_build(word_dict):
        graph = collections.defaultdict(list)
        queue = set([beginWord])
        word_dict.discard(beginWord)
        while queue:
            nxt = set()
            for word in queue:
                # construct new word and add to new
                for i in range(len(word)):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + char + word[i + 1:]
                        if new_word in word_dict and new_word not in graph and new_word not in queue:
                            graph[word].append(new_word)
                            nxt.add(new_word)
            queue = nxt
            if endWord in queue:
                return graph
        return []


    def dfs(sofar, cur):
        if cur == endWord:
            res.append(sofar[:])
            return
        for neigh in graph[cur]:
            dfs(sofar + [neigh], neigh)

    word_dict = set(wordList)
    if endWord not in word_dict:
        return []
    graph = bfs_build(word_dict)
    print(graph)
    if not graph:
        return []
    res = []
    dfs([beginWord], beginWord)
    return res
beginWord = "red"
endWord = "tax"
wordList = ["ted","tex","red","tax","tad","den","rex","pee"]
print(findLadders(beginWord,endWord,wordList))