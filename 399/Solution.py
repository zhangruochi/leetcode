"""
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0. 
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? . 
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
"""

from collections import defaultdict
class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = defaultdict(dict)
        ans = []
        for index, (a,b) in enumerate(equations):
            graph[a][b] = values[index]
            graph[b][a] = 1.0/values[index]
        
        
        def dfs_rec(x,y,visited,cum):
        
            if x == y:
                ans.append(cum)
                return
            visited.add(x)
            
            for n in graph[x]:
                if n not in visited:
                    dfs_rec(n,y,visited,cum*graph[x][n])
                    
                    
            
            
        
        for query in queries:
            start,end = query[0],query[1]
            if start not in graph or end not in graph:
                ans.append(-1.0)
                continue
            dfs_rec(graph,start,end,1,set())
        
        return ans
                    
                    
                
            
            
            
            
            
        
        
        
            
        