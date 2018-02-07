class Solution1:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 is "0" or num2 is "0":
            return "0"
        pos = [[] for i in range(len(num1) + len(num2))]
        startIndex = 0
        for i in range(len(num2) - 1, -1, -1):
            curStartIndex = 0
            for j in range(len(num1) - 1, -1, -1):
                cur = str(int(num2[i]) * int(num1[j]))
                curIndex = 0
                for k in range(len(cur) - 1, -1, -1):
                    pos[startIndex + curStartIndex + curIndex].append(cur[k])
                    curIndex += 1
                curStartIndex += 1
            startIndex += 1

        res = ""
        carry = 0
        index = 0
        while index < len(pos) or carry:
            val = carry
            for cur in pos[index]:
                val += int(cur)
            carry = int(val / 10)
            res = str(val % 10) + res
            index += 1
        return res.lstrip("0")


class Solution2:
    def multiply(self, num1, num2):
        res = 0
        for i in range(len(num1)):
            res *= 10
            n = int(num1[i])
            temp_n = 0
            for j in range(len(num2)):
                temp_n *= 10
                temp_n += int(num2[j]) * n
            res += temp_n
        return str(res)


s = Solution1()
num1 = "999"
num2 = "999"
res = s.multiply(num1, num2)
print(res)
