class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        count = 0
        for i in range(0, len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            if i == 0 and i != len(flowerbed) - 1 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                count += 1
            elif i != len(flowerbed) - 1 and flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                count += 1
            elif i == len(flowerbed) - 1 and flowerbed[i - 1] == 0:
                flowerbed[i] = 1
                count += 1
        return n <= count
