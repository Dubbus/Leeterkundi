'''
nums = [-1,0,1,2,-1,-4]
sorted nums:
 [-4,-1,-1,0,1,2]
 l = 0 
 k = -4 

'''





class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = [] 
        #sort the array to apply two pointers
        nums.sort() 

        for i,k in enumerate(nums):
            # k automatically updates 
            if i > 0 and k == nums[i-1]:
                continue
            
            l = i + 1 
            r = len(nums) - 1

            while l < r: 
                sum = nums[l] + nums[r] + k
                if sum > 0: 
                    r -= 1
                elif sum < 0: 
                    l += 1
                else: 
                    result.append([k, nums[l], nums[r]])
                    l += 1 
                    r -= 1 
                    while l < r and nums[l] == nums[l-1]:
                        l += 1 
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1 

                    
        return result
            


            
