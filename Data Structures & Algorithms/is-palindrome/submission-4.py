class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = "".join(c for c in s.lower() if c.isalnum())
        l = 0
        r = len(filtered) - 1
        while l < r:
            if filtered[l] != filtered[r]:
                return False
            l += 1
            r -= 1
        return True
                