class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        res = len(nums)
        while start <= end:
            mid = int((start + end) / 2)

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                res = mid
                end = mid - 1

        return res


sol = Solution()
nums = [1]
target = 0
print(sol.searchInsert(nums, target))
