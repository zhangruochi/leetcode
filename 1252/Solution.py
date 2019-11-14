class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        if not n or not m or not indices:
            return 0
        
        matrix = {(r,c):0 for r in range(n) for c in range(m)}
        for r,c in indices:
            for key in matrix.keys():
                if r == key[0]:
                    matrix[key] += 1
                if c == key[1]:
                    matrix[key] += 1
        
        return sum([1 if value % 2 != 0 else 0 for value in matrix.values()])
                   
            