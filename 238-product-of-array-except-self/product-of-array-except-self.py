class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #need to solve this problem in O(n) without using division operator 
        result = [1] * (len(nums))
        #prefix pass 
        prefix = 1
        for n in range(len(nums)):
            result[n] = prefix
            prefix = nums[n] * prefix 


        postfix = 1
        #postfix pass 
        for n in range(len(nums) -1, -1, -1):
            result[n] = postfix * result[n]
            postfix *= nums[n]

        return result