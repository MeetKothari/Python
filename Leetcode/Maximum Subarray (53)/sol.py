class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSub = nums[0] # start this value here, eventually want to return 
        curr = 0    # init the container for the running total
        
        for n in nums: # for the number in nums
            if curr < 0:    # if there's a neg prefix
                curr = 0 
            curr += n
            maxSub = max(maxSub, curr)
        return maxSub
        
