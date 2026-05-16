class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1 

        while l < r: 
            curSum = numbers[l] + numbers[r]
            if curSum > target: 
                #move right pointer left
                r -= 1
            
            elif curSum < target: 
                #move left pointer right 
                l += 1
            else: 
                return [1 + l, r + 1]
        return [] 
