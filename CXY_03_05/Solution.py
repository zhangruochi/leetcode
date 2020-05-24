"""
栈排序。 编写程序，对栈进行排序使最小元素位于栈顶。最多只能使用一个其他的临时栈存放数据，但不得将元素复制到别的数据结构（如数组）中。该栈支持如下操作：push、pop、peek 和 isEmpty。当栈为空时，peek 返回 -1。

示例1:

 输入：
["SortedStack", "push", "push", "peek", "pop", "peek"]
[[], [1], [2], [], [], []]
 输出：
[null,null,null,1,null,2]
示例2:

 输入： 
["SortedStack", "pop", "pop", "push", "pop", "isEmpty"]
[[], [], [], [1], [], []]
 输出：
[null,null,null,null,null,true]
说明:

栈中的元素数目在[0, 5000]范围内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-of-stacks-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 思想和单调栈的思想差不多，当入栈的元素val大于栈顶时用辅助栈来保存弹出的数据
# 当栈顶元素大于等于val时入栈，然后将help栈的元素圧回data栈;

class SortedStack:

    def __init__(self):
        self.s1 = []
        self.s2 = []


    def push(self, val: int) -> None:
        while self.s1 and val > self.s1[-1]:
            self.s2.append(self.s1.pop())
        
        self.s1.append(val)

        while self.s2:
            self.s1.append(self.s2.pop())


    def pop(self) -> None:
        if self.isEmpty():
            return -1
        else:
            return self.s1.pop()


    def peek(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.s1[-1]



    def isEmpty(self) -> bool:
        return len(self.s1) == 0



# Your SortedStack object will be instantiated and called as such:
# obj = SortedStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.peek()
# param_4 = obj.isEmpty()