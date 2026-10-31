from collections import defaultdict
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack =[]
        max_a=0
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>heights[i]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1]-1
                max_a = max(max_a,h*w)
            stack.append(i)
        return max_a