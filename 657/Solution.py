class Solution:
    def judgeCircle(self, moves: str) -> bool:
        move_map = {"U":0,"D":0,"L":0,"R":0}
        for char in moves:
            move_map[char]  += 1
        
        if move_map["U"] - move_map["D"] == 0 and move_map["L"] - move_map["R"] == 0:
            return True
        else:
            return False