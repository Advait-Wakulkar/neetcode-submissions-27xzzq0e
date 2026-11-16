class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        res = set()
        maxLen = 1
        if len(s) == 0 :
            return 0
        else:
            for right in range(len(s)):
                while s[right] in res:
                    res.remove(s[left])
                    left += 1
                res.add(s[right])
                maxLen = max(maxLen, right - left + 1)
        return maxLen



        