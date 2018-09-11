class Trie(object):

    def __init__(self):
        self.root_node = {}

    def add_word(self, word):
        current_node = self.root_node
        is_new_word = False

        # Work downwards through the trie, adding nodes
        # as needed, and keeping track of whether we add
        # any nodes.
        for char in word:
            if char not in current_node:
                is_new_word = True
                current_node[char] = {}
            current_node = current_node[char]

        # Explicitly mark the end of a word.
        # Otherwise, we might say a word is
        # present if it is a prefix of a different,
        # longer word that was added earlier.
        if "End Of Word" not in current_node:
            is_new_word = True
            current_node["End Of Word"] = {}



    def search(self, word, current_node):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """

        for i in range(len(word)):

            if word[i] == '.':
                return any([self.search(word[i+1:],current_node[key]) for key in current_node.keys()])

            elif word[i] in current_node:
                current_node = current_node[word[i]]
            else:
                return False

        if "End Of Word" in current_node:
            return True
        return False








t = Trie()
t.add_word('bad')
t.add_word('dad')
t.add_word('mad')
print(t.search('mad',t.root_node))
#print(t.search('mad',t.root_node))




str1 = 'dhruv'
str2 = 'bhg'

#print(set(str2) - set(str1))