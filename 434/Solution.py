"""
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5
"""

class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())

    

    def countSegments2(self,s):
        count,index,length = 0,0,len(s)
        
        while index < length:
            while index < length and s[index] == ' ':
                index += 1
            
            if index < length:
                count += 1
                
            while index < length and s[index] != ' ':
                index += 1


        return count

if __name__ == '__main__':
    print(Solution().countSegments2("abc "))
                    


