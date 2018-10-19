class QuickFind:
    def __init__(self,n):
        self.count = n
        self.id = [0] * self.count

    # initialize N sites with integer names    
    def union(self,p,q): 
        id_p = self.id[p]
        if not self.connected(p,q):
            for i in range(len(self.id)):
                if self.id[i] == id_p:
                    self.id[i] = self.id[q]
            self.count -= 1        

    
    # return component identifier for p
    def find(self,p): 
        return self.id[p]
    
    # return true if p and q are in the same component
    def connected(self,p,q): 
        return self.find(p) == self.find(q)

    # number of components    
    def count(self): 
        return self.count




class QuickUnion:
    def __init__(self,n):
        self.count = n
        self.id = [0] * self.count

    # initialize N sites with integer names    
    def union(self,p,q): 
        id_q = self.find(q)
        id_p = self.find(p)

        # 根节点相连
        if not self.connected(p,q):
            self.id[id_p] = id_q
            self.count -= 1 
    
    # return component identifier for p
    def find(self,p): 
        # 根节点的值为自己
        while p != self.id[p]:
            p = self.id[p]
        return p
    
    # return true if p and q are in the same component
    def connected(self,p,q): 
        return self.find(p) == self.find(q)

    # number of components    
    def count(self): 
        return self.count



class WeightedQuickUnion:
    def __init__(self,n):
        self.count = n
        self.id = [0] * self.count
        self.sz = [1] * self.count

    # initialize N sites with integer names    
    def union(self,p,q): 
        id_q = self.find(q)
        id_p = self.find(p)

        # 根节点相连
        if not self.connected(p,q):
            # 将小节点附在大节点上
            if(self.sz[id_q] < self.sz[id_p]):
                self.id[id_q] = id_p
                self.sz[id_p] = self.sz[id_p] + self.sz[id_q]
            else:
                self.id[id_p] = id_q
                self.sz[id_q] = self.sz[id_q] + self.sz[id_p]

            self.count -= 1 
    
    # return component identifier for p
    def find(self,p): 
        # 根节点的值为自己
        while p != self.id[p]:
            p = self.id[p]
        return p
    
    # return true if p and q are in the same component
    def connected(self,p,q): 
        return self.find(p) == self.find(q)

    # number of components    
    def count(self): 
        return self.count


if __name__ == '__main__':
    #qf = QuickFind(10)
    qf = QuickUnion(10)
    print("initial id list is %s" % (",").join(str(x) for x in qf.id))

    list = [
            (4,3),
            (3,8),
            (6,5),
            (9,4),
            (2,1),
            (8,9),
            (5,0),
            (7,2),
            (6,1),
            (1,0),
            (6,7)
            ]

    for k in list:
        p =  k[0]
        q =  k[1]
        qf.union(p,q)
        print("%d and %d is connected? %s" % (p,q,str(qf.connected(p,q)    )))
        
    print("final id list is %s" % (",").join(str(x) for x in qf.id))
    print("count of components is: %d" % qf.count)
