"""
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。

 

示例:

输入: [1,2,3,4,5]
输出: [120,60,40,30,24]
 

提示：

所有元素乘积之和不会溢出 32 位整数
a.length <= 100000


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def constructArr(self, a: List[int]) -> List[int]:

        prefix_prod = [1]
        suffix_prod = [1]
        res = []

        for num in a:
            prefix_prod.append( prefix_prod[-1] * num)

        for i in range(len(a)-1, -1, -1):
            suffix_prod.append(suffix_prod[-1] * a[i])
        
        suffix_prod.reverse()

        for a, b in zip(prefix_prod[0:-1], suffix_prod[1:]):
            res.append(a*b)

        return res


