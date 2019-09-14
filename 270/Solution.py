"""
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4
"""

import bisect

class Solution(object):
    
    def inorder(self,root,nums):
        if not root:
            return 
        self.inorder(root.left,nums)
        nums.append(root.val)
        self.inorder(root.right,nums)
        
    # time complexity O(n), space complexity O(n)
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        nums = []
        self.inorder(root,nums)
        pos = bisect.bisect(nums,target)
        
        if pos == len(nums):
            return nums[-1]
        elif pos == 0:
            return nums[0]
        else:
            return nums[pos-1] if target - nums[pos-1] < nums[pos] - target else nums[pos]


class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        min_ = float("inf")
        while root:
            tmp = abs(target - root.val)
            if tmp < min_:
                min_ = tmp
                result = root.val
                    
            if root.val > target:
                root = root.left
            elif root.val < target:
                root = root.right
            else:
                return root.val
        return result



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        
        
        
        res = None
        min_diff = float("inf")
        
        def traverse(root):
            nonlocal res,min_diff
            
            if not root: return 
            
            if abs(root.val - target) < min_diff:
                min_diff = abs(root.val - target)
                res = root.val
                
            
            if root.val < target:
                traverse(root.right)
            else:
                traverse(root.left)
            
        
        traverse(root)
        
        return res
