from collections import Counter
from functools import reduce
class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        M = 10**9 + 7
        
        def combination(m,n):
            return reduce(lambda x,y: x*y, [i for i in range(m-n+1,m+1)]) // reduce(lambda x,y: x*y, [i for i in range(1,n+1)])

        count = Counter(A)
        res = 0
        A.sort()
        
        for index, num in enumerate(A):
            # print(num)
            sum_ = target - num
            count[num] -= 1  # 防止往前找 
            i, j = index + 1, len(A)-1
            
            while i < j:
                if A[i] + A[j] < sum_:
                    i += 1
                elif A[i] + A[j] > sum_:
                    j -= 1
                else:
                    # print(num, A[i], A[j])
                    if A[i] == A[j]:
                        res += combination(count[A[i]], 2)
                    else:
                        res += count[A[i]] * count[A[j]]
                    # print("res",res)
                    i += count[A[i]]
                    j -= count[A[j]]
        
        return res % M
                
                    
            