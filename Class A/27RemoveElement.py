class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        i = count = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
                i -= 1
            else:
                count += 1
            i += 1

        return count
