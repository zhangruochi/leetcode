"""
In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to closest person.

Example 1:

Input: [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
Example 2:

Input: [1,0,0,0]
Output: 3
Explanation: 
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
Note:

1 <= seats.length <= 20000
seats contains only 0s or 1s, at least one 0, and at least one 1.
"""

class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        max_,prev = 0,0
        flag = True
        for index,seat in enumerate(seats):
            if seat == 1:    
                dis = index - prev
                prev = index
                # 第一个
                if flag:
                    max_ = max(max_,dis)
                    flag = False
                # 中间
                max_ = max(max_,dis//2)
        # 最后一个      
        max_ = max(max_,len(seats)-1-prev)
        return max_

class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        indics = []
        for i,num in enumerate(seats):
            if num > 0:
                indics.append(i)

        max_dis = max(indics[0], len(seats) - indics[-1] - 1)    
        for i in range(len(indics) -1):
            max_dis = max(max_dis,(indics[i+1] - indics[i])//2)
        
        return max_dis

from itertools import groupby

class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        ans = 0
        for seat, group in itertools.groupby(seats):
            if not seat:
                ans = max(ans, (len(list(group)) + 1)//2)
        
        return max(ans,seats.index(1),seats[::-1].index(1))
    

        
        
        
        
        
                

