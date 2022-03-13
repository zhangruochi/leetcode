"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.


Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        
        def helper(i,pos,num):
            if pos == len(nums):
                return 
            
            for i in range(pos, len(nums)):
                if i != pos and nums[i-1] == nums[i]:
                    continue
                num.append(nums[i])
                res.append(num[:])
                helper(pos,i+1,num)
                num.pop()
        
        helper(0, 0, [])
        res.append([])
        
        return res
        
        

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def helper(pos, path):
            res.append(path[:])

            visited = set()

            for i in range(pos, len(nums)):
                # if i > pos and nums[i] == nums[i-1]:
                #     continue

                if nums[i] in visited:
                    continue
                else:
                    visited.add(nums[i])

                path.append(nums[i])
                helper(i + 1, path)
                path.pop()

        helper(0, [])

        return res