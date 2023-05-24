# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    print(f"in def v: {version}")
    if version >= 1702766719:
        return True
    else:
        return False


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 1, n
        while start < end:
            mid = int((start+end)/2)
            if isBadVersion(mid):
                end = mid
            else:
                start = mid + 1

        return start

        # for version in range(n, 0, -1):
        #     if not isBadVersion(version):
        #         return version + 1
        # return 1


sol = Solution()
print(sol.firstBadVersion(2126753390))
