"""
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
Example 2:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False

"""

class Solution:
    def inorder(self,root,nums):
        if not root:
            return 
        self.inorder(root.left,nums)
        nums.append(root.val)
        self.inorder(root.right,nums)
        
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        nums = []
        self.inorder(root,nums)
        low,high = 0,len(nums)-1
        while low < high:
            tmp = nums[low] + nums[high]
            if tmp < k:
                low += 1
            elif tmp > k:
                high -= 1
            else:
                return True
        return False

