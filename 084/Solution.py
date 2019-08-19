```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        max_stack = []
        heights.append(0)
        for i in range(len(heights)):
            while max_stack and heights[max_stack[-1]] >= heights[i]:
                cur = max_stack.pop()
                if not max_stack: 
                    max_area = max(max_area, heights[cur] * i)
                else:
                    max_area = max(max_area,heights[cur]*(i - max_stack[-1] - 1))
            max_stack.append(i)
        
        return max_area
```