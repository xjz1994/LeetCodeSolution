MorseCode = {
    'a': '.-',     'b': '-...',   'c': '-.-.',
    'd': '-..',    'e': '.',      'f': '..-.',
    'g': '--.',    'h': '....',   'i': '..',
    'j': '.---',   'k': '-.-',    'l': '.-..',
    'm': '--',     'n': '-.',     'o': '---',
    'p': '.--.',   'q': '--.-',   'r': '.-.',
    's': '...',    't': '-',      'u': '..-',
    'v': '...-',   'w': '.--',    'x': '-..-',
    'y': '-.--',   'z': '--..'
}


class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        codeSet = set()
        for i in words:
            s = ""
            for c in i:
                s += MorseCode[c]
            codeSet.add(s)
        return len(codeSet)


s = Solution()
words = ["gin", "zen", "gig", "msg"]
res = s.uniqueMorseRepresentations(words)
print(res)
