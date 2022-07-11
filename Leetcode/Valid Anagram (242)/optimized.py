class Solution:
    def isAnagram(self, s: str, t:str) -> bool:
      return Counter(s) == Counter(t)




# Runtime: 52 ms, faster than 89.14% of Python3 online submissions for Valid Anagram.
# Memory Usage: 14.5 MB, less than 66.72% of Python3 online submissions for Valid Anagram.
