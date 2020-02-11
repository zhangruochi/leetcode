class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        
        # L ... R  => L ... R
        
        # R ... L  => R R . L L   # odd
        # R ....L =>  R R R L L L # even
        
        # R ... R  => R R R R R
        # L ... L  => L L L L L
        
        res = list(dominoes)
        
        items = [(-1, 'L')] + [(i,x) for i,x in enumerate(dominoes) if x != "." ] + [(len(dominoes), 'R')]
        
        
        for (i,x),(j,y) in zip(items[0:-1], items[1:]):
            if x == y:
                for index in range(i+1,j):
                    res[index] = x
            elif x > y:
                i += 1; j -= 1
                while i < j:
                    res[i] = x; res[j] = y
                    i += 1; j -= 1
                            
        return "".join(res)
                    
                    
                
        
            