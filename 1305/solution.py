"""
Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order.

 

Example 1:


Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]
Example 2:

Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output: [-10,0,0,1,2,5,7,10]
Example 3:

Input: root1 = [], root2 = [5,1,7,0,2]
Output: [0,1,2,5,7]
Example 4:

Input: root1 = [0,-10,10], root2 = []
Output: [-10,0,10]
Example 5:


Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]
 

Constraints:

Each tree has at most 5000 nodes.
Each node's value is between [-10^5, 10^5].
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        def in_order(root, res):
            if not root:
                return []
            
            in_order(root.left, res)
            res.append(root.val)
            in_order(root.right, res)
            
            return  res
        
        
        array1 = in_order(root1, [])
        array2 = in_order(root2, [])
        
        res = []
        l,r = 0,0
        while l < len(array1) and r < len(array2):
            if array1[l] < array2[r]:
                res.append(array1[l])
                l+=1
            else:
                res.append(array2[r])
                r+=1
        
        if l < len(array1):
            res += array1[l:]
        else:
            res += array2[r:]
            
        return res
                
            
            
            
            