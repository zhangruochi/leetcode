"""
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
"""

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def find_parent(i):
            if parent[i] == i:
                return i
            else:
                return find_parent(parent[i])

        def union(i, j):
            # merge tree_j to tree_i
            parent[find_parent(j)] = find_parent(i)
        
        proviances = len(isConnected)
        parent = list(range(proviances))

        for i in range(proviances-1):
            for j in range(i+1, proviances):
                if isConnected[i][j]:
                    union(i,j)
        
        return sum([ parent[i] == i for i in range(proviances) ])