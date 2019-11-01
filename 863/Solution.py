# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from collections import defaultdict

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        
        if root == None or target == None:
            return []
                
        def tree_traverse(root,parent, graph):
            if not root:
                return 
            if root.left:
                graph[root.val].append(root.left.val)
            if root.right:
                graph[root.val].append(root.right.val)
            if parent:
                graph[root.val].append(parent.val)
            
            tree_traverse(root.left,root, graph)
            tree_traverse(root.right,root, graph)
            
            return graph
            
            
        def dfs(graph,target, K, visited, res):
            if K == 0:
                res.append(target)
                return res
            
            for node in graph[target]:
                if node not in visited:
                    visited.add(node)
                    dfs(graph,node, K-1, visited, res)
                    visited.remove(node)
                    
            return res
        
        return dfs(tree_traverse(root,None,defaultdict(list)),target.val,K, set([target.val]), [])
        
    
        