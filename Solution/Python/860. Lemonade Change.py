class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five = 0
        ten = 0
        for i in bills:
            if i == 5:
                five += 1
            elif i == 10:
                if five >= 1:
                    ten += 1
                    five -= 1
                else:
                    return False
            elif i == 20:
                if five >= 1 and ten >= 1:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True


# bills = [5, 5, 5, 10, 20]
bills = [10, 10]
res = Solution().lemonadeChange(bills)
print(res)
