# Given the integer n representing the number of courses at some university labeled from 1 to n, and the array dependencies where dependencies[i] = [xi, yi]  represents a prerequisite relationship, that is, the course xi must be taken before the course yi.  Also, you are given the integer k.
#
# In one semester you can take at most k courses as long as you have taken all the prerequisites for the courses you are taking.
#
# Return the minimum number of semesters to take all courses. It is guaranteed that you can take all courses in some way.
#
#  
# Example 1:
#
#
#
#
# Input: n = 4, dependencies = [[2,1],[3,1],[1,4]], k = 2
# Output: 3 
# Explanation: The figure above represents the given graph. In this case we can take courses 2 and 3 in the first semester, then take course 1 in the second semester and finally take course 4 in the third semester.
#
#
# Example 2:
#
#
#
#
# Input: n = 5, dependencies = [[2,1],[3,1],[4,1],[1,5]], k = 2
# Output: 4 
# Explanation: The figure above represents the given graph. In this case one optimal way to take all courses is: take courses 2 and 3 in the first semester and take course 4 in the second semester, then take course 1 in the third semester and finally take course 5 in the fourth semester.
#
#
# Example 3:
#
#
# Input: n = 11, dependencies = [], k = 2
# Output: 6
#
#
#  
# Constraints:
#
#
# 	1 <= n <= 15
# 	1 <= k <= n
# 	0 <= dependencies.length <= n * (n-1) / 2
# 	dependencies[i].length == 2
# 	1 <= xi, yi <= n
# 	xi != yi
# 	All prerequisite relationships are distinct, that is, dependencies[i] != dependencies[j].
# 	The given graph is a directed acyclic graph.
#
#


class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        r = [[] for _ in range(n + 1)]
        rev = [[] for _ in range(n + 1)]
        for e in dependencies:
            r[e[0]].append(e[1])
            rev[e[1]].append(e[0])
        cnt = 0
        steps = 0
        isok = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            if len(rev[i]) == 0:
                isok[i] = 1
        # learned = [0 for _ in range(n + 1)]
        learned = set([])
        while cnt < n:
            tolearn = []
            order = sorted(range(1, n + 1), key = lambda x: - len(r[x]))
            for i in order:
                if isok[i] and i not in learned:
                    tolearn.append(i)
                    learned.add(i)
                    cnt += 1
                    if len(tolearn) == k:
                        break
            for j in tolearn:
                for neib in r[j]:
                    rev[neib].remove(j)
            # print(rev)
            for i in range(1, n + 1):
                if len(rev[i]) == 0:
                    isok[i] = 1
            # print(tolearn)
            steps += 1
        return steps
        