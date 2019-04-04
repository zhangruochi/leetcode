from collections import Counter
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        table = Counter(S)
        return sum(table.get(char,0) for char in set(J))
    
        

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        set_j = set(J)
        count = 0
        for char in S:
            if char in set_j:
                count += 1
        return count

    def numJewelsInStones(self, J, S):
        return sum(map(J.count, S))