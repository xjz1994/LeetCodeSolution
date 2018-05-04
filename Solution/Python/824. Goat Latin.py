class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowelSet = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        arr = S.split(" ")
        maStr = "maa"
        for i in range(len(arr)):
            s = arr[i]
            if(s[0] in vowelSet):
                arr[i] = s + maStr
            else:
                arr[i] = s[1:] + s[0] + maStr

            maStr = maStr + "a"

        return " ".join(arr)


s = Solution()
S = "The quick brown fox jumped over the lazy dog"
res = s.toGoatLatin(S)
print(res)
