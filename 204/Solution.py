"""
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""
class Solution:
    # 时间复杂度高
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        def isPrime(num):
            if num < 2:
                return False
            if num == 2:
                return True
            for i in range(2,num//2+1):
                if num % i == 0:
                    return False
            return True
        
        count = 0
        for i in range(n):
            if isPrime(i):
                count+= 1
        return count  

    def countPrimes2(self,n):
        if n < 3:
            return 0
        count_mask = [1] * n
        count_mask[0] = count_mask[1] = 0

        for i in range(2,int(n**0.5) + 1):
            if count_mask[i]:
                count_mask[i*i:n:i] = [0] * len(count_mask[i*i:n:i])
                
        return sum(count_mask)


# class Solution:
#     def countPrimes(self, n: int) -> int:
#         if n < 2:
#             return 0
        
        
#         def isPrime(num):
#             for i in range(2,num//2+1):
#                 if num % i == 0:
#                     return False
#             return True
        
        
#         count = 0
#         for num in range(2,n):
#             if isPrime(num):
#                 count += 1
                
#         return count

# class Solution:
#     def countPrimes(self, n: int) -> int:
#         if n < 2:
#             return 0
        
        
#         def isPrime(num):
#             for i in range(2,int(num**0.5)+1):
#                 if num % i == 0:
#                     return False
#             return True
        
        
#         count = 0
#         for num in range(2,n):
#             if isPrime(num):
#                 count += 1
                
#         return count

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        n = n-1
        positions = [False] * n
        
        
        def isPrime(num):
            if num == 2:
                return True
            
            for i in range(2,int(num**0.5)+1):
                if num % i == 0:
                    return False
            return True
        
        
        def mask(positions, base, n):
            i = 1
            while True:
                if base*i > n:
                    break
                positions[base*i-1] = True
                i += 1
                
        count = 0
        
        for base in range(2, int(n**0.5)+1):
            if (not positions[base-1]) and isPrime(base):  
                mask(positions, base, n)
                count += 1

        for _ in positions:
            if _ == False:
                count += 1
            
            
        return count - 1

if __name__ == '__main__':
    solution = Solution()
    print(solution.countPrimes(10000) == solution.countPrimes2(10000))
                
