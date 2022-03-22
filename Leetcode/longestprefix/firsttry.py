# Runtime: 36 ms, faster than 87.49% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 14 MB, less than 21.98% of Python3 online submissions for Longest Common Prefix.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        shortest , longest = min(strs),max(strs)
        for i in range(len(shortest)):
            if shortest[i]==longest[i]:
                result +=shortest[i]
            else:
                break
        return result
