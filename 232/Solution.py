"""
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
Notes:

You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
"""

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not len(self.stack):
            return None
        tmp = []
        
        while self.stack:
            tmp.append(self.stack.pop())
        top = tmp.pop()
        
        while tmp:
            self.stack.append(tmp.pop())
        return top  
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not len(self.stack):
            return None

        tmp = []
        while self.stack:
            tmp.append(self.stack.pop())

        top = tmp[-1]
        while tmp:
            self.stack.append(tmp.pop())
        return top
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack) == 0




class MyQueue:

    def __init__(self):
        self.stack = []
        self.buffer = []


    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        res = None
        while self.stack:
            self.buffer.append(self.stack.pop())
        
        res = self.buffer.pop()
        while self.buffer:
            self.stack.append(self.buffer.pop())
        return res

    def peek(self) -> int:
        res = None
        while self.stack:
            self.buffer.append(self.stack.pop())
        
        res = self.buffer[-1]
        while self.buffer:
            self.stack.append(self.buffer.pop())
        return res


    def empty(self) -> bool:
        return len(self.stack) == 0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


if __name__ == '__main__':
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    print(queue.peek())
    print(queue.pop())
    print(queue.empty())
    









