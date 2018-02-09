class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        arr = [i for i in str(x)]
        return arr == arr[::-1]


s = Solution()
s.isPalindrome(-2147483648)
