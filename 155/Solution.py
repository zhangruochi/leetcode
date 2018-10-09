"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.array = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.array) == 0:
            min = x 
        elif self.getMin() > x:
            min = x
        else:
            min = self.getMin()

        self.array.append((x,min)) 


    def pop(self):
        """
        :rtype: void
        """
        if not self.array:
            return None
        else:
            return self.array.pop()[0]    
        

    def top(self):
        """
        :rtype: int
        """
        if not self.array:
            return None
        else:
            return self.array[-1][0]    
        

    def getMin(self):
        """
        :rtype: int
        """
        if not self.array:
            return None

        return self.array[-1][1] 


if __name__ == '__main__':


    # Your MinStack object will be instantiated and called as such:
    minStack = MinStack();
    minStack.push(0)
    minStack.push(1)
    minStack.push(0)
    print(minStack.getMin())   #--> Returns -3.
    print(minStack.pop())
    #print(minStack.top())      #--> Returns 0.
    print(minStack.getMin())   #--> Returns -2.