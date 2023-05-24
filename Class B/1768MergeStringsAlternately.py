class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        if not word1:
            return word2
        if not word2:
            return word1

        res = ''
        ptr1 = 0
        ptr2 = 0
        while ptr1 < len(word1) and ptr2 < len(word2):
            res += word1[ptr1] + word2[ptr2]
            ptr1 += 1
            ptr2 += 1

        while ptr1 < len(word1):
            res += word1[ptr1]
            ptr1 += 1

        while ptr2 < len(word2):
            res += word2[ptr2]
            ptr2 += 1

        return res

#
# sol = Solution()
# word1 = 'abc'
# word2 = 'pqr'
# print(sol.mergeAlternately(word1, word2))
