class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        pref = 1
        for num in nums:
            res.append(pref)
            pref *= num
        post = 1
        for i in range(len(nums) - 1 , -1 , -1):
            res[i] *= post
            post *= nums[i]
        return res
        