"""
Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.
Example 1:

MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5
Note:

-1e7 <= x <= 1e7
Number of operations won't exceed 10000.
The last four operations won't be called when stack is empty.
"""



class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.all_nums  = []
        self.current_max = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        
        self.all_nums.append(x)
        
        if not self.current_max:
            self.current_max.append(x)
        elif x > self.current_max[-1]:
            self.current_max.append(x)
        else:
            self.current_max.append(self.current_max[-1])

        

    def pop(self):
        """
        :rtype: int
        """
        self.current_max.pop()
        return self.all_nums.pop()
    
    
    def top(self):
        """
        :rtype: int
        """
        if self.all_nums:
            return self.all_nums[-1]
        

    def peekMax(self):
        """
        :rtype: int
        """
        if self.current_max:
            return self.current_max[-1]
        

    def popMax(self):
        """
        :rtype: int
        """
        tmp_stack = []
        max = self.current_max[-1]
        while True:
            tmp = self.all_nums.pop()
            self.current_max.pop()
            if tmp == max:
                break
            else:
                tmp_stack.append(tmp)
        
        while tmp_stack:
            self.push(tmp_stack.pop())
        
        return max
            
            
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()