class Solution:
    def countLetters(self, S: str) -> int:
        if not S:
            return 1
        
        def cum_sum(n):
            return (1+n)*n//2
        
        cur = 1
        res = 0
        prev = S[0]
        for char in S[1:]:
            if char == prev:
                cur += 1
            else:
                res += cum_sum(cur)
                cur = 1
                prev = char
        res += cum_sum(cur)
        return res
        