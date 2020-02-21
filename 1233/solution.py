class Node():
    def __init__(self, str_):
        self.str_ = str_
        
    def __eq__(self, other):
        return self.str_ == other.str_
    
    def __repr__(self):
        return self.str_
    
    def __repr__(self):
        return self.str_
    
    def __hash__(self):
        return hash(self.str_)
    
    def __call__(self,str_):
        return Node(str_)
        
    
        
    
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        trie = {}
        res = []
               
        def transfrom(f):
            return list(map(Node, f.strip("/").split("/")))
            

        folder = list( map(transfrom, folder))
        
        print(folder)
        
        for f in folder:
            trie_pointer = trie
            for char in f:
                trie_pointer = trie_pointer.setdefault(char, {})
            trie_pointer["#"] = "#"
    
    
        def combine(path):
            return "/"+"/".join([str(node) for node in path])
    
        def dfs(trie, path):
            nonlocal res
            if "#" in trie:
                res.append(combine(path))
                return 
            
            for char in trie:
                path.append(char)
                dfs(trie[char],path)
                path.pop()
        dfs(trie, [])
        
        return res
        