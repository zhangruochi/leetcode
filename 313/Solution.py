"""
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.

Example:

Input: n = 12, primes = [2,7,13,19]
Output: 32 
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 
             super ugly numbers given primes = [2,7,13,19] of size 4.
Note:

1 is a super ugly number for any given primes.
The given numbers in primes are in ascending order.
0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
"""

import heapq
class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        count = 0
        heap = [1]
        pool = set([1])
        while True:
            num = heapq.heappop(heap)
            for ugly in (num*prime for prime in primes):
                if ugly in pool:
                    continue
                else:
                    pool.add(ugly)
                    heapq.heappush(heap,ugly)
            count += 1
            if count == n:
                return num

import heapq
class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        pointers = [0] * len(primes)
        ugly_seris = [1]
        
        while len(ugly_seris) < n:
            min_ = float("inf")
            tmp_i = -1
            for i in range(len(primes)):
                if  primes[i] * ugly_seris[pointers[i]] < min_:
                    min_ = primes[i] * ugly_seris[pointers[i]]
                    tmp_i = i
                ugly_seris.append(min_)
                pointers[tmp_i] += 1
        return ugly_seris[-1]


class Solution:
    """时间复杂度高"""
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        pointers = [0] * len(primes)
        ugly_seris = [1]
        
        while len(ugly_seris) < n:
            min_ = float("inf")
            tmp_i = -1
            for i in range(len(primes)):
                tmp_nums = primes[i] * ugly_seris[pointers[i]]
                if  tmp_nums < min_:
                    min_ = tmp_nums
                    tmp_i = i
            pointers[tmp_i] += 1
            if min_ != ugly_seris[-1]:
                ugly_seris.append(min_)

        return ugly_seris[-1]