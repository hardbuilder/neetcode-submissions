class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_a=0
        i = 0
        j = len(heights)-1
        while i<j:
            a = min(heights[i],heights[j])*(j-i)
            max_a=max(max_a,a)
            if heights[i]<=heights[j]:
                i+=1
            else:
                j-=1
        return max_a