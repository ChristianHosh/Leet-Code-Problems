class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        max_candies = max(candies)
        res = []
        for kid_candies in candies:
            res.append(kid_candies + extraCandies >= max_candies)

        return res
