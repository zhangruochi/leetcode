from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
    
        count = Counter(nums)
        sorted_count = sorted(count.items(), key = lambda x:x[1], reverse = True)
        ans = []
        for i in range(k):
            ans.append(sorted_count[i][0])
        return ans
        
        
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [pair[0] for pair in Counter(nums).most_common(k)]
        