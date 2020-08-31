# -*- coding:utf-8 -*-


# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Example 1:
#
#
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#
#
# Example 2:
#
#
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
#
#  
# Constraints:
#
#
# 	1 <= n <= 45
#
#


class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if (n <= 3):
            return n
        else:
            M = [0 for _ in range(n + 1)]
            M[2] = 2
            M[3] = 3
            for i in range(4, n + 1):
                M[i] = M[i - 1] + M[i - 2]
            return M[n]
        
