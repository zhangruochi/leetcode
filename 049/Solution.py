from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = defaultdict(list)
        for word in strs:
            ans["".join(sorted(word))].append(word)
        
        return list(ans.values())
        