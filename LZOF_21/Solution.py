"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

 

示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4] 
注：[3,1,2,4] 也是正确的答案之一。
 

提示：

1 <= nums.length <= 50000
1 <= nums[i] <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        odd = 0; even = len(nums) - 1
    
        while odd < even:
            
            while odd < len(nums) and nums[odd] % 2 != 0:
                odd += 1
            
            while even >= 0 and nums[even] % 2 == 0:
                even -= 1

            if odd < len(nums) and even >= 0 and odd < even:
                nums[odd],nums[even] = nums[even], nums[odd]

        return nums
            