class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        arr = list(S)
        left = 0
        right = len(S) - 1

        while left < right:
            while left < right and not arr[left].isalpha():
                left += 1
            while left < right and not arr[right].isalpha():
                right -= 1
            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        return "".join(arr)


S = "Test1ng-Leet=code-Q!"
res = Solution().reverseOnlyLetters(S)
print(res)
