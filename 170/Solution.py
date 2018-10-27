"""
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example 1:

add(1); add(3); add(5);
find(4) -> true
find(7) -> false
Example 2:

add(3); add(1); add(2);
find(3) -> true
find(6) -> false

"""

from collections import defaultdict

class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.count = 0
        self.numbers = defaultdict(list)
        

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.numbers[number].append(self.count)
        self.count += 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for num, indexs in self.numbers.items():
            tmp = value - num
            if tmp in self.numbers:
                if tmp == num and len(indexs) > 1:
                    return True
                if tmp != num:
                    return True
        return False