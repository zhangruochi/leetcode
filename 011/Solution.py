class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        front,end = 0,len(height)-1
        most_water = 0
        while front < end:
            most_water = max(most_water,min(height[front],height[end]) * (end - front))
            if height[front] < height[end]:
                front += 1
            else:
                end -= 1
        return most_water