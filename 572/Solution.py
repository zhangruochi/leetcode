"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""

class Solution:
    
    def DFS(self,s,t):
        
        if not t and not s:
            return True
        elif not s or not t:
            return False

        return s.val == t.val and self.DFS(s.left,t.left) and self.DFS(s.right,t.right)
        
    
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s:
            return 
        
        queue = deque([s])
        while queue:
            cur_node = queue.popleft()
            print(cur_node.val)
            if self.DFS(cur_node,t):
                return True
            if cur_node.left: 
                queue.append(cur_node.left)
            if cur_node.right:    
                queue.append(cur_node.right)
        return False


class Solution:
    
    def DFS(self,s,t):
        
        if not t and not s:
            return True
        elif not s or not t:
            return False

        return s.val == t.val and self.DFS(s.left,t.left) and self.DFS(s.right,t.right)

        

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s:
            return False
        return  self.DFS(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t) 


      
        

        
    


