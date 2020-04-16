
## TLE

```python
class Solution:
    def checkValidString(self, s: str) -> bool:
        
        # "((((*))"
        def helper(s, stack):
  
            for i, char in enumerate(s):
                if char == "(":
                    stack.append("(")
                elif char == ")":
                    if not stack:
                        return False
                    else:
                        stack.pop()
                else:
                    return helper( "" + s[i+1:], stack[:]) or helper( "(" + s[i+1:], stack[:]) or helper( ")" + s[i+1:], stack[:])
                            
            
            if not stack:
                return True
            else:
                return False
        
        return helper(s,[])
```