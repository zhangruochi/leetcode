"""
Design your implementation of the circular double-ended queue (deque).

Your implementation should support following operations:

MyCircularDeque(k): Constructor, set the size of the deque to be k.
insertFront(): Adds an item at the front of Deque. Return true if the operation is successful.
insertLast(): Adds an item at the rear of Deque. Return true if the operation is successful.
deleteFront(): Deletes an item from the front of Deque. Return true if the operation is successful.
deleteLast(): Deletes an item from the rear of Deque. Return true if the operation is successful.
getFront(): Gets the front item from the Deque. If the deque is empty, return -1.
getRear(): Gets the last item from Deque. If the deque is empty, return -1.
isEmpty(): Checks whether Deque is empty or not. 
isFull(): Checks whether Deque is full or not.
 

Example:

MyCircularDeque circularDeque = new MycircularDeque(3); // set the size to be 3
circularDeque.insertLast(1);            // return true
circularDeque.insertLast(2);            // return true
circularDeque.insertFront(3);           // return true
circularDeque.insertFront(4);           // return false, the queue is full
circularDeque.getRear();            // return 2
circularDeque.isFull();             // return true
circularDeque.deleteLast();         // return true
circularDeque.insertFront(4);           // return true
circularDeque.getFront();           // return 4
"""

class MyCircularDeque:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.queue = [None] * k
        self.front, self.tail = 0,0
        self.length = k
        

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if not self.isFull():
            self.queue[self.front] = value
            self.front = (self.front - 1) % self.length
            return True
        return False
        
        

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if not self.isFull():
            self.tail = (self.tail + 1) % self.length
            self.queue[self.tail] = value
            return True
        return False
            
        

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if not self.isEmpty():
            self.front = (self.front + 1) % self.length
            self.queue[self.front] = None
            return True
        return False
        
            
            
    
    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if not self.isEmpty():
            self.queue[self.tail] = None
            self.tail = (self.tail - 1) % self.length
            return True
        return False
        

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if not self.isEmpty():
            return self.queue[(self.front+1)%self.length]
        else:
            return -1
        

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if not self.isEmpty():
            return self.queue[self.tail]
        else:
            return -1

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return True if (self.front == self.tail and not self.queue[self.front]) else False
        

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return True if (self.front == self.tail and self.queue[self.front]) else False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()