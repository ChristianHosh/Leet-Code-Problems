class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        placed = 0
        i = 0
        if flowerbed == [0]:
            return True

        while i < len(flowerbed):
            if flowerbed[i] == 0:
                if i == 0 and flowerbed[i + 1] == 0:
                    placed += 1
                    flowerbed[i] = 1
                elif i == len(flowerbed) - 1 and flowerbed[i - 1] == 0:
                    placed += 1
                    flowerbed[i] = 1
                elif flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                    placed += 1
                    flowerbed[i] = 1

            i += 1

        return placed >= n

#
# sol = Solution()
# flowerbed = [1, 0, 0, 0, 0]
# n = 1
# print(sol.canPlaceFlowers(flowerbed, n))
