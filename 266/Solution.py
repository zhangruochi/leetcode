from collections import Counter

class Solution:
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
        
        table = Counter(s)
        counts = list(table.values())

        
        if len(counts) == 1:
            return True
        
        
        if sum(counts) % 2 == 0:
            for count in counts:
                if count % 2 != 0:
                    return False
            return True
        else:
            count_odd = 0
            
            for count in counts:
                if count % 2:
                    count_odd += 1
    
            return count_odd == 1