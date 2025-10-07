class Solution:
    def maxArea(self, height: List[int]) -> int:
        h=height
        n=len(height)
        l=0
        max_area = 0
        res=0
        r=n-1
        ml=0
        mr=0
        while l<r:
            width = r - l
            max_area = max(max_area, min(height[l], height[r]) * width)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1 
        return max_area
