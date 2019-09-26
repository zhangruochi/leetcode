"""
You have a set of tiles, where each tile has one letter tiles[i] printed on it.  Return the number of possible non-empty sequences of letters you can make.

 

Example 1:

Input: "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: "AAABBC"
Output: 188
 

Note:

1 <= tiles.length <= 7
tiles consists of uppercase English letters.
"""



from itertools import permutations
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()
        def func(item):
            return "".join(item)
            
        for i in range(1,len(tiles)+1):
            res.update(list(map(func, permutations(tiles, i))))
        
        return len(res)

from collections import Counter
# from itertools import permutations
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = []
        char_dict = Counter(tiles)
        
        def helper(char_dict,string):
            nonlocal res
            for key in char_dict:
                if char_dict[key] > 0:
                    char_dict[key] -= 1
                    string += key
                    res.append(string)
                    helper(char_dict,string)
                    char_dict[key] += 1
        helper(char_dict,"")
        return len(res)
                    
                    
                    
                
            
        