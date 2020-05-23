"""
三合一。描述如何只用一个数组来实现三个栈。

你应该实现push(stackNum, value)、pop(stackNum)、isEmpty(stackNum)、peek(stackNum)方法。stackNum表示栈下标，value表示压入的值。

构造函数会传入一个stackSize参数，代表每个栈的大小。

示例1:

 输入：
["TripleInOne", "push", "push", "pop", "pop", "pop", "isEmpty"]
[[1], [0, 1], [0, 2], [0], [0], [0], [0]]
 输出：
[null, null, null, 1, -1, -1, true]
说明：当栈为空时`pop, peek`返回-1，当栈满时`push`不压入元素。
示例2:

 输入：
["TripleInOne", "push", "push", "push", "pop", "pop", "pop", "peek"]
[[2], [0, 1], [0, 2], [0, 3], [0], [0], [0], [0]]
 输出：
[null, null, null, null, 2, 1, -1, -1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/three-in-one-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class TripleInOne:

    def __init__(self, stackSize: int):
    
        self.start = {0:0, 1:stackSize, 2: 2*stackSize}

        self.stack_index = {0:[0, stackSize-1], 
                            1:[stackSize, 2*stackSize-1], 
                            2:[2*stackSize, 3*stackSize-1]}

        self.array = [None] * stackSize * 3

    def push(self, stackNum: int, value: int) -> None:
        if not self.isFull(stackNum):
            self.array[self.stack_index[stackNum][0]] = value
            self.stack_index[stackNum][0] += 1
    

    def pop(self, stackNum: int) -> int:
        if not self.isEmpty(stackNum):
            self.stack_index[stackNum][0] -= 1
            res = self.array[self.stack_index[stackNum][0]]
            self.array[self.stack_index[stackNum][0]] = None
            return res
        else:
            return -1


    def peek(self, stackNum: int) -> int:
        if not self.isEmpty(stackNum):
            return self.array[self.stack_index[stackNum][0]-1]
        else:
            return -1
            
    def isEmpty(self, stackNum: int) -> bool:
        return self.stack_index[stackNum][0] == self.start[stackNum]


    def isFull(self, stackNum) -> bool:
        return (self.stack_index[stackNum][0] - 1) == self.stack_index[stackNum][1]





# Your TripleInOne object will be instantiated and called as such:
# obj = TripleInOne(stackSize)
# obj.push(stackNum,value)
# param_2 = obj.pop(stackNum)
# param_3 = obj.peek(stackNum)
# param_4 = obj.isEmpty(stackNum)