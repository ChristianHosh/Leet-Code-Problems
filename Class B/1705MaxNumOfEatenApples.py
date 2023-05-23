import heapq


class Solution(object):
    def eatenApples(self, apples, days):
        """
        :type apples: List[int]
        :type days: List[int]
        :rtype: int
        """
        n = len(days)
        day = 1
        count = 0
        queue = []

        


#
if __name__ == '__main__':
    sol = Solution()
    testcases_apples = {0: [3,1,1,0,0,2],
                        1: [1,2,3,5,2],
                        2:[3,0,0,0,0,2],

                        }
    testcases_days = {0: [3,1,1,0,0,2],
                      1: [3,2,1,4,2],
                      2: [3,0,0,0,0,2],

                      }

    testcases_exp = {0: 5,
                     1: 7,
                     2: 5,
                     }

    for i in range(len(testcases_days)):
        print(f"************\nTEST CASE {i}")
        print(f"OUTPUT: {sol.eatenApples(testcases_apples[i],testcases_days[i])}\n"
              f"Expected: {testcases_exp[i]}")
