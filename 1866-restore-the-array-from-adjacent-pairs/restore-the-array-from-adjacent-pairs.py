"""There is an integer array nums that consists of n unique elements, but you have forgotten it. However, you do remember every pair of adjacent elements in nums.

You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are adjacent in nums.

It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will exist in adjacentPairs, either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]]. The pairs can appear in any order.

Return the original array nums. If there are multiple solutions, return any of them.
"""

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for a , b in adjacentPairs:
            g[a].append(b)
            g[b].append(a)
        
        start = next(x for x in g if len(g[x]) == 1)
        res = [start]
        prev = None

        while len(res) < len(g):
            cur = res[-1]
            nxt = g[cur][0] if g[cur][0]!= prev else g[cur][1]
            res.append(nxt)
            prev = cur

        return res