"""
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:

Input: 
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.
Example 2:

Input: 
    2
   / \
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
"""
# Definition for a binary tree node.


from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """        
        def get_all_value(root,result):
            if root == None:
                return 
            else:
                result.append(root.val)
                get_all_value(root.left,result)    
                get_all_value(root.right,result)

        def find_second(nodes):
            diff_nodes = set(nodes)
            if len(diff_nodes) <=1:
                return -1
            else:
                return sorted(list(diff_nodes))[1]    

        nodes = []
        get_all_value(root,nodes)

        return find_second(nodes)

     
    def findSecondMinimumValue2(self,root):
        """广度优先搜索
        """

        if not root:
            return -1

        queue = deque()
        queue.append(root)
        
        min_node, second_min, found = root.val, float('inf'), False

        while queue:
            cur_node = queue.popleft()
            if cur_node.val > min_node and cur_node.val < second_min:
                second_min = cur_node.val
                found = True
                continue

            if not cur_node.left:
                continue

            queue.append(cur_node.left)
            queue.append(cur_node.right)

        return  second_min if found else -1    

    def findSecondMinimumValue3(self,root):

        if not root:
            return -1

        min_num = root.val    

        def DFS(root,min_num):
            if not root:
                return -1
        
            if root.val > min_num:
                return root.val

            min_l = DFS(root.left,min_num)
            min_r = DFS(root.right,min_num)

            if min_l == -1:
                return min_r

            if min_r == -1:
                return  min_l    

            return min(min_l,min_r)
        
        return DFS(root,min_num)  



        











