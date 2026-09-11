class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = [] 
        maxheight = 0 
        l = 0 
        r = len(height) - 1
        while l < r: 
            #calculate area here
            area =  (r - l) * min(height[l], height[r])
            result.append(area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        maxheight = max(result)
        return maxheight
            