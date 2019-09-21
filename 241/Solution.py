"""
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation: 
((2-1)-1) = 0 
(2-(1-1)) = 2
Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
"""



from operator import add,mul,sub
from itertools import product
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        opr_map = {"+":add,"*":mul,"-":sub}
        # opr_map = {"+": lambda x,y : x+y, 
        #    "*": lambda x,y : x*y,
        #    "-": lambda x,y : x-y
        #   }
        memory = dict()
        
        def ways(input):
            if input in memory:
                return memory[input]
            ans = []
            for i,char in enumerate(input):
                if char in opr_map:
                    ans += [opr_map[char](l,r) for l,r in product(ways(input[:i]), ways(input[i+1:]))]
            if not ans: 
                ans.append(int(input))
            memory[input] = ans 
            return ans
        
        return ways(input)
                
                

            
            
        