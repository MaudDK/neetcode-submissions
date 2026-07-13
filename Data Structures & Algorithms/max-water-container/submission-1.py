class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            area = self.calculateArea(l, r, heights)
            max_area = max(max_area, area)

            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        
        return max_area

    
    def calculateArea(self, l, r, heights):
        side = min(heights[l], heights[r])
        length = r-l
        return side * length




        