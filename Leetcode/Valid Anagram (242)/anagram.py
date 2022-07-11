class Solution:
    def isAnagram(self, s: str, t:str) -> bool:
        
        countS, countT = {}, {}
        
        if len(s) != len(t): return False
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
            
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True
      
# Runtime: 86 ms, faster than 36.66% of Python3 online submissions for Valid Anagram.
# Memory Usage: 14.6 MB, less than 34.56% of Python3 online submissions for Valid Anagram.
