"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.

"""

class Solution:
    """超过时间复杂度"""

    def is_ugly(self,number):
        while number % 2 == 0:
            number //= 2
        
        while number % 3 == 0:
            number //= 3
        
        while number % 5 == 0:
            number //= 5

        return number == 1
            
        
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        number = 0
        while count != n:
            number += 1
            if self.is_ugly(number):
                count +=1    

        return number


class Solution:
    def nthUglyNumber(self, n):
        result = [1]
        p1,p2,p3 = 0,0,0

        while len(result) < n:

            x1 = result[p1]*2
            x2 = result[p2]*3
            x3 = result[p3]*5

            num = min(x1,min(x2,x3))

            if num == x1:
                p1 += 1
            elif num == x2:
                p2 += 1
            elif num == x3:
                p3 += 1

            if num != result[-1]:
                result.append(num)

        return result[n-1]

import heapq
class Solution:
    def nthUglyNumber(self,n):
        pool = set()
        heap = []
        number_series = [1]
        count = 0

        while True:
            num = heapq.heappop(number_series)
            for ex in (num*2,num*3,num*5):
                if ex in pool:
                    continue
                else:
                    pool.add(ex)
                    heapq.heappush(number_series,ex)
            count += 1  

            if count == n:
                return num  


import heapq
class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 
        pool,count = set([1]),0
        heap = [1]
        heapq.heapify(heap)
        while True:
            cur = heapq.heappop(heap)
            count += 1
            if count == n:
                return cur
            
            for num in (cur*2,cur*3,cur*5):
                if num not in pool:
                    pool.add(num)
                    heapq.heappush(heap,num)
        return -1
            

import heapq
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        heap = [1]
        visited = set(heap)
        heapq.heapify(heap)
        index = 0
        
        while index < n:
            item = heapq.heappop(heap)
            index += 1
            if item*2 not in visited:
                heapq.heappush(heap,item*2)
                visited.add(item*2)
            
            if item*3 not in visited:
                heapq.heappush(heap,item*3)
                visited.add(item*3)
                
            if item*5 not in visited:
                heapq.heappush(heap,item*5)
                visited.add(item*5)
        
        
        return item
        


if __name__ == '__main__':
    print(Solution().nthUglyNumber(10))





