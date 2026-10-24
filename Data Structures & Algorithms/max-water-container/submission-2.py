class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        p1, p2 = 0,len(heights)-1
        area = 0


        for i in range(len(heights)-1):
            p1, p2  = i, i + 1
            while p2 < len(heights):
            
                area = max((p2 - p1) * min(heights[p1], heights[p2]), area) 
                p2+=1

        return area 