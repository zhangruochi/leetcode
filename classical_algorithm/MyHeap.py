## heap sort make poor use of cache memory

class minBinaryHeap:
    """ 最小堆
    """
    def __init__(self,lists = []):
        self.heap_list = lists
        self.curret_size = len(lists)
        self.heapify()

    def shiftup(self,i):
        if i == 0 or self.heap_list[i] >= self.heap_list[(i-1)//2]:
            return

        self.heap_list[i],self.heap_list[(i-1)//2] = self.heap_list[(i-1)//2],self.heap_list[i]

        return self.shiftup((i-1)//2)


    def shiftdown(self,i):
        # 左右结点都不存在 到达叶子结点
        if i * 2 + 1 > self.curret_size-1:
            return 

        # 左右结点都存在    
        if i * 2 + 2 <= self.curret_size-1:
            if self.heap_list[i] <= self.heap_list[i*2+1] and self.heap_list[i] <= self.heap_list[i*2+2]:
                return
            else:
                _min = i*2+1 if self.heap_list[i*2+1] < self.heap_list[i*2+2] else i*2+2
                self.heap_list[i],self.heap_list[_min] = self.heap_list[_min],self.heap_list[i]
                self.shiftdown(_min)
        # 只存在左结点
        else: 
            if self.heap_list[i] <= self.heap_list[i*2+1]:
                return 
            else:
                self.heap_list[i],self.heap_list[i*2+1] = self.heap_list[i*2+1],self.heap_list[i]
                self.shiftdown(i*2+1)


    def insert(self,k):
        self.curret_size += 1
        self.heap_list.append(k)
        self.shiftup(self.curret_size-1)


    def heapify(self,lists = None):
        if lists:
            self.heap_list = lists
            self.curret_size = len(lists)

        for i in range((self.curret_size-2)//2,-1,-1):
            self.shiftdown(i)
            #print(i)
            #print(self.heap_list)
            #exit()

    def getmin(self):
        self.heap_list[0],self.heap_list[self.curret_size-1] = self.heap_list[self.curret_size-1],self.heap_list[0]
        self.curret_size -= 1
        min_item = self.heap_list.pop()
        self.shiftdown(0)
        return min_item


    def isempty(self):
        return self.curret_size == 0  
    

    ## 原地排序  先建堆，然后每次把堆顶的元素与堆尾的元素交换，然后把堆的 size - 1
    @staticmethod
    def heap_sort(iterable):
        heap = minBinaryHeap(iterable)        
        while heap.curret_size:
            heap.heap_list[0],heap.heap_list[heap.curret_size-1] = heap.heap_list[heap.curret_size-1],heap.heap_list[0]
            heap.curret_size -= 1
            heap.shiftdown(0)
        return heap.heap_list    




if __name__ == '__main__':
    from random import randint    
    values = [randint(0,100) for i in range(10)]

    myheap = minBinaryHeap(values)
    myheap.insert(70)
    myheap.insert(20)

    sorted_values = []
    while not myheap.isempty():
        sorted_values.append(myheap.getmin())

    print(sorted_values)    

    #原地排序
    sorted_values = minBinaryHeap.heap_sort([9,8,7,6,5,4,3,2,1])
    print(sorted_values)
    exit()




## ------------- heapq 的使用 -------------------
import heapq

# 建堆 
data = [1,5,3,2,8,5]
heap = []
for n in data:
    heapq.heappush(heap,n)

data = [1,5,3,2,8,5]
heapq.heapify(data)


# 最小元素访问
print(heapq.heappop(data))


# 删除现有最小元素并替换成新值，可以使用heapreplace()
print(heapq.heapreplace(data,10))
print(data)


# nlargest and nsmallest
print(heapq.nlargest(3, data))
print(heapq.nsmallest(3, data))


## 堆排序
def heapsort(iterable):
    h = []
    heapq.heapify(iterable)
    return [heapq.heappop(iterable) for i in range(len(iterable))]

print(heapsort([9,8,7,6,5,4,3,2,1]))






                


                
                