"""
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.
For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:

The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".
"""


class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        result = []
        for hour in range(0, 12):
            time = ""
            if bin(hour).count("1") <= num:
                time += str(hour)
                for i in range(60):
                    if bin(i).count("1") == (num - bin(hour).count("1")):
                        if i < 10:
                            result.append(time + ":0" + str(i))
                        else:
                            result.append(time + ":" + str(i))

        return result

    def bit_count(self, number):
        count = 0
        while number:
            number = number & (number - 1)
            count += 1
        return count

    def readBinaryWatch2(self, num):
        return ["{0}:{1:02d}".format(hour, minute) for hour in range(12) for minute in range(60)
                if self.bit_count(hour) + self.bit_count(minute) == num]



class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        return ["{0}:{1:02d}".format(hour,mins) for hour in range(12) for mins in range(60) if bin(hour).count("1") + bin(mins).count("1") == num]

if __name__ == '__main__':
    print(Solution().readBinaryWatch2(5))
