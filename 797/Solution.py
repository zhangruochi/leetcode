"""
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).


Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

"""

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        if not graph or not graph[0]:
            return []
        
        all_path = []

        def visited(graph, path, node):
            nonlocal all_path

            if node == len(graph)-1:
                all_path.append(list(path))

            for next_node in graph[node]:
                visited(graph, path + [next_node], next_node)
            

        visited(graph, [0], 0)

        return all_path