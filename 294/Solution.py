"""
You are playing a Flip Game with your friend.

You are given a string currentState that contains only '+' and '-'. You and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move, and therefore the other person will be the winner.

Return true if the starting player can guarantee a win, and false otherwise.


Example 1:

Input: currentState = "++++"
Output: true
Explanation: The starting player can guarantee a win by flipping the middle "++" to become "+--+".
Example 2:

Input: currentState = "+"
Output: false

Constraints:

1 <= currentState.length <= 60
currentState[i] is either '+' or '-'.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/flip-game-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""



class Solution:
    def canWin(self, currentState: str) -> bool:

        # 枚举每一种情况，然后递归到下一层，看对手可不可以赢，如果对手有赢得情况那么就无法保证一定能赢   
        # 所以 canWin 这个函数的意思是 "在当前这种状态下，至少有一种选法，能够让他赢"。而 (!canWin) 的意思就变成了 "在当前这种状态下，无论怎么选，都不能赢"。

        state_map = {}

        def helper(currentState):
            nonlocal state_map

            if currentState in state_map:
                return state_map[currentState]

            for i in range(len(currentState)-1):
                if currentState[i:i+2] == "++":
                    flip = currentState[:i] + "--" + currentState[i+2:]
                    if not self.canWin(flip):
                        state_map[currentState] = True
                        return True

            state_map[currentState] = False
            return False

        return helper(currentState)
            