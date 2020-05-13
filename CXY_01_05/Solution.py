"""
字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。

 

示例 1:

输入: 
first = "pale"
second = "ple"
输出: True
 

示例 2:

输入: 
first = "pales"
second = "pal"
输出: False

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/one-away-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        

        if len(first) < len(second):
            first, second = second , first
        m,n = len(first), len(second)

        diff = m - n
        flag = 0

        if diff > 1:
            return False
        elif diff == 1:
            i , j = 0, 0
            while j < n:
                if first[i] != second[j]:
                    i+= 1
                    flag += 1
                    if flag > 1:
                        return False
                else:
                    i += 1; j += 1
            
            return True
        else:
            i, j = 0, 0 
            while j < n:
                if first[i] != second[j]:
                    flag += 1
                    if flag > 1:
                        return False
                
                i+= 1; j+= 1
            return  True
                

