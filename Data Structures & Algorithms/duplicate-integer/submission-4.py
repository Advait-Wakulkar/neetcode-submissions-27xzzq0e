class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        N = len(set(nums))
        n = len(nums)
        if N == n :
            return False
        else :
            return True
        