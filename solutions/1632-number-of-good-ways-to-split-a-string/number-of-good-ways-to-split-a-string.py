# You are given a string s, a split is called good if you can split s into 2 non-empty strings p and q where its concatenation is equal to s and the number of distinct letters in p and q are the same.
#
# Return the number of good splits you can make in s.
#
#  
# Example 1:
#
#
# Input: s = "aacaba"
# Output: 2
# Explanation: There are 5 ways to split "aacaba" and 2 of them are good. 
# ("a", "acaba") Left string and right string contains 1 and 3 different letters respectively.
# ("aa", "caba") Left string and right string contains 1 and 3 different letters respectively.
# ("aac", "aba") Left string and right string contains 2 and 2 different letters respectively (good split).
# ("aaca", "ba") Left string and right string contains 2 and 2 different letters respectively (good split).
# ("aacab", "a") Left string and right string contains 3 and 1 different letters respectively.
#
#
# Example 2:
#
#
# Input: s = "abcd"
# Output: 1
# Explanation: Split the string as follows ("ab", "cd").
#
#
# Example 3:
#
#
# Input: s = "aaaaa"
# Output: 4
# Explanation: All possible splits are good.
#
# Example 4:
#
#
# Input: s = "acbadbaada"
# Output: 2
#
#
#  
# Constraints:
#
#
# 	s contains only lowercase English letters.
# 	1 <= s.length <= 10^5
#


class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)
        c = Counter(s)
        lc = Counter("")
        ans = 0
        nofl = 0
        nofr = len(c.keys())
        for i in range(n):
            if s[i] not in lc:
                nofl += 1
            lc[s[i]] += 1
            c[s[i]] -= 1
            if c[s[i]] == 0:
                nofr -= 1
            if nofl == nofr:
                ans += 1
        return ans
            