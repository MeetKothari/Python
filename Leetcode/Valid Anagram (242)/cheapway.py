class Solution:
    def isAnagram(self, s: str, t:str) -> bool:
      return sorted(s) == sorted(t)

# Runtime: 109 ms, faster than 12.62% of Python3 online submissions for Valid Anagram.
# Memory Usage: 15.2 MB, less than 11.52% of Python3 online submissions for Valid Anagram.
