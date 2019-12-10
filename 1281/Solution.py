from functools import reduce
from operator import mul,add
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = list(map(int,str(n)))
        return reduce(mul,n) - reduce(add,n)