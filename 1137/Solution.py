class Solution:
    def tribonacci(self, n: int) -> int:
        
        memory = {}
        
        def helper(n):
            nonlocal memory
            
            if n in memory:
                return memory[n]
        
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 1

            res = helper(n-1) + helper(n-2) + helper(n-3)
            memory[n] = res
            
            return res
        
        return helper(n)