# Runtime: 126 ms, faster than 15.65% of Python3 online submissions for Palindrome Number.
# Memory Usage: 13.8 MB, less than 68.09% of Python3 online submissions for Palindrome Number.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
        
