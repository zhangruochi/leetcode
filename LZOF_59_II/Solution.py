"""
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。

若队列为空，pop_front 和 max_value 需要返回 -1

示例 1：

输入: 
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]
示例 2：

输入: 
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]
 

限制：

1 <= push_back,pop_front,max_value的总操作数 <= 10000
1 <= value <= 10^5


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from collections import deque

class MaxQueue:

    def __init__(self):
        self.data = deque([])
        self.max_ = deque([])


    def max_value(self) -> int:
        if self.empty:
            return -1
        return self.max_[0]


    def push_back(self, value: int) -> None:
        self.data.append(value)


        # 保证单调性
        while self.max_ and value > self.max_[-1]:
            self.max_.pop()
        
        self.max_.append(value)


    def pop_front(self) -> int:
        if self.empty:
            return - 1

        value = self.data.popleft()
        
        if value == self.max_[0]:
            self.max_.popleft()

        return value

    @property
    def empty(self):
        return len(self.data) == 0



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()