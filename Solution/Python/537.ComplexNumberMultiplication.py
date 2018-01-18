
class Solution(object):
    def complexNumberMultiply(self, a, b):
        import re
        pattern = re.compile("-*\d+")
        numA = int(pattern.findall(a)[0])
        numB = int(pattern.findall(a)[1])
        numC = int(pattern.findall(b)[0])
        numD = int(pattern.findall(b)[1])
        real = numA * numC - numB * numD
        imaginary = numB * numC + numA * numD
        return str(real) + "+" + str(imaginary) + "i"
