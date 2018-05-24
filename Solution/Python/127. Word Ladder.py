class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordSet = set(wordList)
        queue = [(beginWord, 1)]
        while queue:
            word, length = queue.pop(0)
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    nextWord = word[:i] + c + word[i+1:]
                    if nextWord in wordSet:
                        wordSet.remove(nextWord)
                        queue.append((nextWord, length + 1))
            return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
res = Solution().ladderLength(beginWord, endWord, wordList)
print(res)
