from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        my_dict = defaultdict(list)
        for index,num in enumerate(nums):
            if my_dict[num] and (index - my_dict[num][-1]) <= k:
                return True         
            my_dict[num].append(index)
        
        return False
    
    def containsNearbyDuplicate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        my_dict = {}
        for index,num in enumerate(nums):
            if num in my_dict  and (index - my_dict[num]) <= k:
                return True         
            my_dict[num] = index

        return False