# table.dungeon, .dungeon th, .dungeon td {
#   border:3px solid black;
# }
#
#  .dungeon th, .dungeon td {
#     text-align: center;
#     height: 70px;
#     width: 70px;
# }
#
# The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.
#
# The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.
#
# Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).
#
# In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.
#
#  
#
# Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.
#
# For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.
#
#
#
#
# 			-2 (K)
# 			-3
# 			3
#
#
# 			-5
# 			-10
# 			1
#
#
# 			10
# 			30
# 			-5 (P)
#
#
#
#
#  
#
# Note:
#
#
# 	The knight's health has no upper bound.
# 	Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.
#
#


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon), len(dungeon[0])
        minHP = [[float('inf')]*m for _ in range(n)]
        tovisit = deque([(n - 1, m - 1)])
        visited = [[False]*m for _ in range(n)]
        minHP[n - 1][m - 1] = max(1, 1-dungeon[n - 1][m - 1])
        while tovisit:
            r, c = tovisit.popleft()
            if visited[r][c]:
                continue
            visited[r][c] = True
            if r - 1 >= 0:
                minHP[r - 1][c] = min(minHP[r - 1][c], max(1, minHP[r][c] - dungeon[r - 1][c]))
                if not visited[r - 1][c]: tovisit.append((r - 1, c))
            if c - 1 >= 0:
                minHP[r][c - 1] = min(minHP[r][c - 1], max(1, minHP[r][c] - dungeon[r][c - 1]))
                if not visited[r][c - 1]: tovisit.append((r, c - 1))
        return minHP[0][0]