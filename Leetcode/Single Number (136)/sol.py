class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # sol must be O(1)
        # constant extra space, no extra stuff like hashmaps
        # you can use bit manipulation, and the XOR 
        # if you XOR, similair values return 0, different values will return 1
        
        result = 0 # initialize, for storing XOR
        for n in nums:
            res = n ^ res
        return res
        
        
        
        
