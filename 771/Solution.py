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