from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = defaultdict(list)
        for word in strs:
            ans["".join(sorted(word))].append(word)
        
        return list(ans.values())



from collections import defaultdict

class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {char:num for char,num in zip("abcdefghijklmnopqrstuvwxyz",range(26))}
        
        def hash_num(string):
            res = [0]*26
            for char in string:
                res[table[char]] += 1
            return "".join(map(str,res))
            
        
        res = defaultdict(list)
        for string in strs:
            res[hash_num(string)].append(string)
        
        return list(res.values())


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        res_dict = defaultdict(list)
        for str_ in strs:
            s_str_ = "".join(sorted(list(str_)))
            res_dict[s_str_].append(str_)
        
        return [res_dict[_] for _ in res_dict ]
                
        