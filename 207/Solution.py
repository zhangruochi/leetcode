class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        G = {node:[] for node in range(numCourses)}
        for edge in prerequisites:
            G[edge[1]].append(edge[0])
        
        
        def top_sort(G):
            in_degree = {node: 0 for node in G}
            
            for u in G:
                for v in G[u]:
                    in_degree[v] += 1
            
            queue = [node for node in in_degree if in_degree[node] == 0]
            res = []
            while queue:
                cur_node = queue.pop()
                res.append(cur_node)
                
                for v in G[cur_node]:
                    in_degree[v] -= 1
                    if in_degree[v] == 0:
                        queue.append(v)
            
            return True if len(res) == len(G) else False
        
        return top_sort(G)
                
            
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def generate_graph(prerequisites):
            graph = {}
            for item in prerequisites:
                if item[0] not in graph:
                    graph[item[0]] = []
                
                if item[1] not in graph:
                    graph[item[1]] = []
                
                graph[item[0]].append(item[1])
            
            return graph
        
        graph = generate_graph(prerequisites)
        print(graph)
        
        
        def dfs_helper(graph, root, visited = None):
            if not visited:
                visited = set()
            
            visited.add(root)
            
            for node in graph[root]:
                if node in visited or dfs_helper(graph, node, visited):
                    return True
            
            visited.remove(root)
            return False
                    
        def detect_cycle(graph):
            
            for root in graph:
                if dfs_helper(graph, root):
                    return True
            
            return False
            
        
        return False if detect_cycle(graph) else True
