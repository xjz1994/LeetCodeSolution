class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        aSum = sum(A)
        bSum = sum(B)
        dif = (aSum - bSum) // 2
        aSet = set(A)
        for b in set(B):
            if dif + b in aSet:
                return [dif + b, b]


# Example 1:
# Input: A = [1,1], B = [2,2]
# Output: [1,2]

# Example 2:
# Input: A = [1,2], B = [2,3]
# Output: [1,2]

# Example 3:
# Input: A = [2], B = [1,3]
# Output: [2,3]

# Example 4:
# Input: A = [1,2,5], B = [2,4]
# Output: [5,4]


A = [1, 2, 5]
B = [2, 4]
res = Solution().fairCandySwap(A, B)
print(res)
