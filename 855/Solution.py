"""
In an exam room, there are N seats in a single row, numbered 0, 1, 2, ..., N-1.

When a student enters the room, they must sit in the seat that maximizes the distance to the closest person.  If there are multiple such seats, they sit in the seat with the lowest number.  (Also, if no one is in the room, then the student sits at seat number 0.)

Return a class ExamRoom(int N) that exposes two functions: ExamRoom.seat() returning an int representing what seat the student sat in, and ExamRoom.leave(int p) representing that the student in seat number p now leaves the room.  It is guaranteed that any calls to ExamRoom.leave(p) have a student sitting in seat p.

 

Example 1:

Input: ["ExamRoom","seat","seat","seat","seat","leave","seat"], [[10],[],[],[],[],[4],[]]
Output: [null,0,9,4,2,null,5]
Explanation:
ExamRoom(10) -> null
seat() -> 0, no one is in the room, then the student sits at seat number 0.
seat() -> 9, the student sits at the last seat number 9.
seat() -> 4, the student sits at the last seat number 4.
seat() -> 2, the student sits at the last seat number 2.
leave(4) -> null
seat() -> 5, the student sits at the last seat number 5.
​​​​​​​

Note:

1 <= N <= 10^9
ExamRoom.seat() and ExamRoom.leave() will be called at most 10^4 times across all test cases.
Calls to ExamRoom.leave(p) are guaranteed to have a student currently sitting in seat number p.
"""


import bisect
class ExamRoom:

    def __init__(self, N):
        """
        :type N: int
        """
        self.seated = []
        self.N = N
        

    def seat(self):
        """
        :rtype: int
        """            
        if not self.seated:
            student = 0
        else:
            max_dis = self.seated[0]
            student = 0
            for prev,cur in zip(self.seated,self.seated[1:]):
                tmp_dis = (cur - prev)//2
                tmp_pos = prev + tmp_dis
                if tmp_dis > max_dis:
                    max_dis = tmp_dis
                    student = tmp_pos
            if self.N-1 - self.seated[-1] > max_dis:
                student = self.N-1
            
        bisect.insort(self.seated,student)
        return student
            
    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        self.seated.remove(p)
        
        

