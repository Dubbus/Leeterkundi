class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countDict = {}
        res = 0 
        l = 0 
        for r in range(len(s)): 
            countDict[s[r]] = 1 + countDict.get(s[r],0)
            
            while (r - l + 1 ) - max(countDict.values()) > k: 
                countDict[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res