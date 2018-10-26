"""
Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:

Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"
Note:

letters has a length in range [2, 10000].
letters consists of lowercase letters, and contains at least 2 unique letters.
target is a lowercase letter.

"""

class Solution(object):
    

    def binary_search(self,letters,target,n):
        low,high = 0,n
     
        while low <= high:
            mid = ((high - low) >> 1) + low
            if ord(letters[mid]) <= ord(target):
                low = mid + 1
            else:
                if mid == 0 or ord(letters[mid-1]) <= ord(target):
                    return letters[mid]
                else:
                    high = mid - 1
        return letters[0]            
                    
    
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        return self.binary_search(letters,target,len(letters)-1)






