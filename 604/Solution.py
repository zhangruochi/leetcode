"""
Design and implement a data structure for a compressed string iterator. It should support the following operations: next and hasNext.

The given compressed string will be in the form of each letter followed by a positive integer representing the number of this letter existing in the original uncompressed string.

next() - if the original string still has uncompressed characters, return the next letter; Otherwise return a white space.
hasNext() - Judge whether there is any letter needs to be uncompressed.

Note:
Please remember to RESET your class variables declared in StringIterator, as static/class variables are persisted across multiple test cases. Please see here for more details.

Example:

StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1");

iterator.next(); // return 'L'
iterator.next(); // return 'e'
iterator.next(); // return 'e'
iterator.next(); // return 't'
iterator.next(); // return 'C'
iterator.next(); // return 'o'
iterator.next(); // return 'd'
iterator.hasNext(); // return true
iterator.next(); // return 'e'
iterator.hasNext(); // return false
iterator.next(); // return ' '
"""

class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.num = 0
        self.string = self.get_string(compressedString)
        self.gen = self.my_gen()
    
    
    def get_string(selif,compressedString):
        res = []
        num = ""
        prev = compressedString[0]
        for char in compressedString:
            if char.isdigit():
                num += char
            
            if num and char.isalpha():
                res.append((int(num),prev))
                num = ""
                prev = char
        
        res.append((int(num),prev))
        
        return res[::-1]
            
    
    def my_gen(self):
        while self.string:
            self.num, char = self.string.pop()
            while self.num > 0:
                self.num -= 1
                yield char
                
            
    def next(self):
        """
        :rtype: str
        """
        return next(self.gen) if self.hasNext() else " "
            
        
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.string or self.num else False
        
        
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()



class StringIterator:

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.position = 0
        self.compressedString = compressedString  
        self.num = self.__next_num()
    
    def __next_num(self):
        i,num = 0, ""
        flag = False
        while i < len(self.compressedString):
            while i < len(self.compressedString) and self.compressedString[i].isdecimal():
                num += self.compressedString[i]
                i+=1
                flag = True
            if flag:
                self.position = i
                break
            i += 1
        return int(num)
    
    def next(self):
        """
        :rtype: str
        """
        ans = " "
        if not self.hasNext():
            return ans
        
        ans = self.compressedString[0]
        self.num -= 1
            
        if self.num == 0:
            self.compressedString = self.compressedString[self.position:]
            if self.hasNext():
                self.num = self.__next_num()
        return ans


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.compressedString != ""
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()