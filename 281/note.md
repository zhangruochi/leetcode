## 思路
- 给出两个数组，返回交替执行的数组
- 创建两个队列，在二者都不为空的时候，轮流从queue中取出元素
- 当某个队列为空时，一直从该队列中取出元素
- 创建一个生成器函数
```Python
def __next(self):
        while self.v1 and self.v2:
            yield self.v1.popleft()
            yield self.v2.popleft()

        while self.v1:
            yield self.v1.popleft() 
        
        while self.v2:
            yield self.v2.popleft()
```
- 调用生成器函数创建一个生成器对象 
```Python
self.genobj = self.__next()
```

- 每次用next函数调用生成器对象，则从队列中取出一个数据
```Python
next(self.genobj)
```
