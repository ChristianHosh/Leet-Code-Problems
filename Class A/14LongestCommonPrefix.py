class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        shortest_str = min(strs, key=len)

        for i, char in enumerate(shortest_str):
            for others_strs in strs:
                if others_strs[i] != char:
                    return shortest_str[:i]

        return shortest_str
