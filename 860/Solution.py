"""
At a lemonade stand, each lemonade costs $5. 

Customers are standing in a queue to buy from you, and order one at a time (in the order specified by bills).

Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.  You must provide the correct change to each customer, so that the net transaction is that the customer pays $5.

Note that you don't have any change in hand at first.

Return true if and only if you can provide every customer with correct change.

 

Example 1:

Input: [5,5,5,10,20]
Output: true
Explanation: 
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.
Example 2:

Input: [5,5,10]
Output: true
Example 3:

Input: [10,10]
Output: false
Example 4:

Input: [5,5,10,10,20]
Output: false
Explanation: 
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can't give change of $15 back because we only have two $10 bills.
Since not every customer received correct change, the answer is false.
 

Note:

0 <= bills.length <= 10000
bills[i] will be either 5, 10, or 20.
"""


class Solution(object):
    
    def is_changed(self,sum_,table):
        
        if not sum_:
            return True
        
        while table[20] > 0 and sum_ - 20 >= 0:
            sum_ -= 20
            table[20] -= 1
            
        while table[10] > 0 and sum_ - 10 >= 0:
            sum_ -= 10
            table[10] -= 1
            
        while table[5] > 0 and sum_ - 5 >= 0:
            sum_ -= 5
            table[5] -= 1
        
        if sum_ == 0:
            return True
        
        return False
            
    
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        table = {5:0,10:0,20:0}
        
        for bill in bills:
            table[bill] += 1
            if not self.is_changed(bill-5,table):
                return False
        return True



class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        counter = {5:0,10:0,20:0}
        for bill in bills:
            change = bill - 5
            if change == 0:
                counter[5] += 1
            elif change == 5:
                while counter[5] > 0 and change - 5 >= 0:
                    counter[5] -= 1
                    change -= 5
                if change:
                    return False
                counter[10] += 1
            else:
                while counter[10] > 0 and change - 10 >= 0:
                    counter[10] -= 1
                    change -= 10
                while counter[5] > 0 and change - 5 >= 0:
                    counter[5] -= 1
                    change -= 5
                if change:
                    return False
                counter[20] += 1
        return True
    
                    
                
            
                
                    
                
        


