class Queue(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * self.capacity
        self.head = 0
        self.tail = 0

    def enqueue(self,x):
        if self.tail == self.capacity:
            ## 如果队满，检查队列头部是否在队始位置，如果不在，进行数据搬移
            if self.head == 0:
                return False
            else:
                for i in range(self.head, self.tail):
                    self.items[i - self.head] = self.items[i]
                    self.items[i] = None
                self.tail -= self.head
                self.head = 0

        self.items[self.tail] = x
        self.tail += 1
        return True

    def dequeue(self):
        if self.head == self.tail:
            return None

        res = self.items[self.head]
        self.items[self.head] = None
        self.head += 1

        return res

    def __repr__(self):
        return str(self.items)


class CircleQueue(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * self.capacity
        self.head = 0
        self.tail = 0

    def enqueue(self,x):
        if (self.tail + 1)%self.capacity == self.head:
            return False
            
        self.items[self.tail] = x
        self.tail  = (self.tail + 1) % self.capacity
        return True

    def dequeue(self):
        if self.head == self.tail:
            return None

        res = self.items[self.head]
        self.items[self.head] = None
        self.head = (self.head + 1) % self.capacity

        return res

    def __repr__(self):
        return str(self.items)



if __name__ == '__main__':
    q = Queue(3)

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.dequeue()
    q.dequeue()
    q.enqueue(4)
    q.enqueue(5)
    q.dequeue()
    q.dequeue()
    q.enqueue(6)
    q.enqueue(7)
    # q.enqueue(4)
    # q.enqueue(5)

    print(q)

    q = CircleQueue(3)

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3) # 失败
    q.dequeue()
    q.dequeue()
    q.enqueue(4)
    q.enqueue(5)
    q.dequeue()
    q.dequeue()
    q.enqueue(6)
    q.enqueue(7)
    q.enqueue(4)
    q.enqueue(5)

    print(q)






