class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        hset = set()
        
        for n in nums:
            if n in hset:
                return True
            hset.add(n)
        
        return False 
      
# Runtime: 478 ms, faster than 90.28% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 26.1 MB, less than 30.48% of Python3 online submissions for Contains Duplicate.
