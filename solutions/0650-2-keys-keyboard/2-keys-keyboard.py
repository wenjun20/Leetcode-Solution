# Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:
#
#
# 	Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
# 	Paste: You can paste the characters which are copied last time.
#
#
#  
#
# Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.
#
# Example 1:
#
#
# Input: 3
# Output: 3
# Explanation:
# Intitally, we have one character 'A'.
# In step 1, we use Copy All operation.
# In step 2, we use Paste operation to get 'AA'.
# In step 3, we use Paste operation to get 'AAA'.
#
#
#  
#
# Note:
#
#
# 	The n will be in the range [1, 1000].
#
#
#  
#


class Solution:
    def bigdiv(self, n):
        for i in range(n - 1, 0, -1):
            if n % i == 0:
                return i
        return 1
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        div = self.bigdiv(n)
        mul = n // div
        return self.minSteps(div) + mul