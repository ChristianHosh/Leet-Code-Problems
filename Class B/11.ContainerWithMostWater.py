class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        start = 0
        end = len(height) - 1

        while start < end:
            area = min(height[start], height[end]) * (end - start)
            max_area = max(area, max_area)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        # for i in range(len(height)):
        #     for j in range(i + 1, len(height)):
        #         min_line = min(height[i], height[j])
        #         bottom_length = j - i
        #         area = min_line * bottom_length
        #         max_area = max(max_area, area)

        return max_area
