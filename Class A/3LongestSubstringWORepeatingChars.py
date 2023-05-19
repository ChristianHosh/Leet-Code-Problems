class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        test = ""
        # Result
        max_length = 0

        if len(s) == 0 or len(s) == 1:
            return len(s)

        for c in s:
            if c in test:
                test = test[test.index(c) + 1:]
            test = test + c
            if max_length < len(test):
                max_length = len(test)
        return max_length


sol = Solution()
print(sol.lengthOfLongestSubstring("abb"))


