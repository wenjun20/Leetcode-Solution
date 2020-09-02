# Given a string S, count the number of distinct, non-empty subsequences of S .
#
# Since the result may be large, return the answer modulo 10^9 + 7.
#
#  
#
# Example 1:
#
#
# Input: "abc"
# Output: 7
# Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".
#
#
#
# Example 2:
#
#
# Input: "aba"
# Output: 6
# Explanation: The 6 distinct subsequences are "a", "b", "ab", "ba", "aa" and "aba".
#
#
#
# Example 3:
#
#
# Input: "aaa"
# Output: 3
# Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".
#
#
#
#
#  
#
#  
#
# Note:
#
#
# 	S contains only lowercase letters.
# 	1 <= S.length <= 2000
#
#
#
#  
#
#
#  
#
#


class Solution:
    def distinctSubseqII(self, S: str) -> int:
        res = [1]
        mod = int(1e9 + 7)
        last = {}
        for i, s in enumerate(S):
            tmp = (res[-1] * 2) % mod
            res.append(tmp)
            if s in last:
                res[-1] -= res[last[s]]
            last[s] = i
        return (res[-1] - 1) % mod