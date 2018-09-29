#!/usr/bin/env python3

# info
# -name   : zhangruochi
# -email  : zrc720@gmail.com


class Solution(object):
    def plusOne_1(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits) - 1
        flag = 1

        while True:

            if flag == 0:
                break

            if flag == 1 and length == -1:
                digits.insert(0, flag)
            elif flag == 1:
                digits[length] = digits[length] + flag

            if digits[length] >= 10:
                digits[length] -= 10
                flag = 1
            else:
                flag = 0

            length -= 1

        return digits

    def plusOne(self, digits):
        number = int("".join(map(str,digits)))
        number += 1
        return list(map(int,list(str(number))))


if __name__ == '__main__':
    solution = Solution()
    print(solution.plusOne([1,9]))
