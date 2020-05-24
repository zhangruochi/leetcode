"""
节点间通路。给定有向图，设计一个算法，找出两个节点之间是否存在一条路径。

示例1:

 输入：n = 3, graph = [[0, 1], [0, 2], [1, 2], [1, 2]], start = 0, target = 2
 输出：true
示例2:

 输入：n = 5, graph = [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3], [3, 4]], start = 0, target = 4
 输出 true
提示：

节点数量n在[0, 1e5]范围内。
节点编号大于等于 0 小于 n。
图中可能存在自环和平行边。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/route-between-nodes-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from functools import reduce
from collections import defaultdict

class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:


        def construct_graph(lists):
            graph = defaultdict(set)
            
            for line in lists:
                graph[line[0]].add(line[1])
    
            for node in graph:
                graph[node] = list(graph[node])

            return graph
        
        graph = construct_graph(graph)

        def dfs(start, visited):
            nonlocal graph,target

            if start == target:
                return True

            if start in visited:
                return False

            ans = False
            visited.add(target)

            for node in graph[start]:                
                ans = ans or dfs(node,visited)
            return ans

        return dfs(start, set())


# class Solution:
#     def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
#         from collections import defaultdict
#         dic = defaultdict(list)
#         for g in graph:
#             dic[g[0]].append(g[1])
#         visted = [False] * n
#         def dfs(vertex, visted):
#             if vertex == target:
#                 return True
#             if visted[vertex]:
#                 return False
#             visted[vertex] = True
#             ans = False
#             for post in dic[vertex]:
#                 ans = ans or dfs(post, visted)
#             return ans
#         return dfs(start, visted)


from functools import reduce
class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:


        def construct_graph(lists):
            graph = defaultdict(set)
            
            for line in lists:
                graph[line[0]].add(line[1])
    
            for node in graph:
                graph[node] = list(graph[node])

            return graph
        
        graph = construct_graph(graph)

        visited = set()
        visited.add(start)
        res = False

        def dfs(start,target, graph):
            nonlocal visited, res

            for node in graph[start]:
                if node == target:
                    res = True
                    return
                
                if node not in visited and not res:
                    visited.add(node)
                    dfs(node,target,graph)


        dfs(start,target,graph)
    
        return res
