class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        for index,num in enumerate(A):
            if index == num:
                return index
        return -1