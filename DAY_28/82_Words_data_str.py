'''Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True'''








# My logic but time limit reached 

class WordDictionary(object):

    def __init__(self):
        self.words = []

    def addWord(self, word):
        self.words.append(word)

    def search(self, word):
        for w in self.words:
            if len(w) != len(word):
                continue
            match = True
            for i in range(len(word)):
                if word[i] != '.' and word[i] != w[i]:
                    match = False
                    break
            if match:
                return True
        return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)









# ChatGPT coded using prefix tree

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        return self._search_in_node(word, self.root)

    def _search_in_node(self, word, node):
        for i, char in enumerate(word):
            if char == '.':
                for child in node.children.values():
                    if self._search_in_node(word[i+1:], child):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                node = node.children[char]
        return node.is_end











# Leet code best solution

from collections import defaultdict as dd, deque as dq

class WordDictionary(object):

    def __init__(self):
        self.dic = dd()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        this = self.dic
        for c in word:
            if c in this:
                this = this[c]
            else:
                this[c] = dd()
                this = this[c]
        this["-"] = None

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        s = dq()
        n = len(word)
        s.append((self.dic, 0))
        while s:
            this, i = s.pop()
            while i < n and word[i] in this:
                this = this[word[i]]
                i += 1
            if i == n:
                if "-" in this:
                    return True
                else:
                    continue 
            if not word[i] == ".":
                continue
            # this char is "."
            for key in this:
                if key == "-":
                    continue
                s.append((this[key], i+1))
        return False


# # Your WordDictionary object will be instantiated and called as such:
# # obj = WordDictionary()
# # obj.addWord(word)
# # param_2 = obj.search(word)


# A better and more efficient solution, by building not a Trie, but just a set

class WordDictionary(object):

    def __init__(self):
        self.d = dict()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        if word:
            self.d[word] = True
            # add words with one dot
            for i in range(len(word)):
                new_word = word[:i]+"."+word[i+1:]
                self.d[new_word] = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if not word:
            return False
        if word in self.d:
            return True
        if word.count('.') < 2:
            return False
        idx = word.index('.')
        for x in range(97, 123):
            new_word = word[:idx] + chr(x) + word[idx+1:]
            if new_word in self.d:
                return True
        return False