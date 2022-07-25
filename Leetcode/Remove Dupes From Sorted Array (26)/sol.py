class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # start at index 0 
        # check nums
        # if nums[i] != nums[i+1]
        # move up one, nums[x] = nums[i+1]
        # at the end, return x, which is final index without the dupe
        
        x = 1
        for i in range(len(nums)-1): # start at 1
            if (nums[i] != nums[i+1]):
                nums[x] = nums[i+1]
                x += 1
        return (x)
                
