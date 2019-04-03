"""
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.


Follow up:
Could you solve it using only O(1) extra space?


Example 1:

Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
Example 2:

Input:
["a"]

Output:
Return 1, and the first 1 characters of the input array should be: ["a"]

Explanation:
Nothing is replaced.
Example 3:

Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.
Note:

All characters have an ASCII value in [35, 126].
1 <= len(chars) <= 1000.
"""


class Solution:

    def get_value_digits(self,value):
        result = []
        while value != 0:
            value,digit = divmod(value,10)
            result.insert(0,str(digit))

        return result 



    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        current_char,count,index,i = None,0,0,0

        while i<len(chars):
            if current_char != chars[i]:
                current_char = chars[i]
                count = 0

            while i<len(chars) and current_char == chars[i]:
                i+=1
                count += 1  

            chars[index] = current_char
            index += 1    
              
            if count == 1:
                pass
            elif count < 10:
                chars[index] = str(count)
                index += 1
            else:
                chars[index:index+len(str(count))] = self.get_value_digits(count)
                index += len(str(count))

        
        #print(chars[:index])
        return index


    def compress2(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        current_char,count,index,i = None,0,0,0

        while i<len(chars):
            if current_char != chars[i]:
                current_char = chars[i]
                count = 0

            while i<len(chars) and current_char == chars[i]:
                i+=1
                count += 1  

            chars[index] = current_char
            index += 1    
              
            if count == 1:
                pass
            else:
                for digit in str(count):
                    chars[index] = digit
                    index += 1
        
        print(chars[:index])
        return index


class Solution:
    def compress(self, chars: List[str]) -> int:
        prev = chars[0]
        index = 0
        count = 0
        for char in chars:
            if char == prev:
                count += 1
            else:
                chars[index] = prev
                index += 1
                if count > 1:
                    for num in str(count):
                        chars[index] = num
                        index += 1
                prev = char
                count = 1
        chars[index] = char
        index += 1

        if count > 1:
            for num in str(count):
                chars[index] = num
                index += 1
        
        return index
            
            
                

        




    

if __name__ == '__main__':
    print(Solution().compress2(["a","a","b","b","c","c","c","c","c","c","c","c","c","c","c","c","a","a"]))     
    
    print(Solution().compress2(['a','b']))
    print(Solution().compress2([]))           
                    
















