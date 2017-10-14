class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        reBin = '{0:b}'.format(n).zfill(32)[::-1]
        return int(reBin, 2)
