from collections import defaultdict
class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        
        if not A or not B:
            return []
        
        index_a,index_b = defaultdict(list),defaultdict(list)
        for i,n in enumerate(A):
            index_a[n].append(i)
        for i,n in enumerate(B):
            index_b[n].append(i)
            
            
        res = [-1] * len(A)
        for key,vals in index_a.items():
            while vals:
                res[vals.pop()] = index_b[key].pop()
        
        return res