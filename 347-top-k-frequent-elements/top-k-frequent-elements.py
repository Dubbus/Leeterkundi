

class Solution:
    #So we have an integer and a list of integers, and we want to return an array of integers.
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Approach: iterate through the list,
        #have a dictionary with frequency as value and number as key
        if k == len(nums):
            return nums

        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        return heapq.nlargest(k, freq.keys(), key = lambda x: freq[x])
      

        