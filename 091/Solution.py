class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
    
        count = 0
        def bfs(i):
            nonlocal count
            if i > len(s):
                return 
            
            if i == len(s):
                count += 1
                return
            
            for j in (1,2):
                if j == 1 and s[i:i+j] == "0": continue
                if j == 2 and ("0" == s[i:i+1] or s[i:i+2] > "26"): break

                bfs(i+j)
                
        bfs(0)
        return count
                
            
        

if __name__ == '__main__':
    solution = Solution()
    s = "4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948"
    print(solution.numDecodings(s))
