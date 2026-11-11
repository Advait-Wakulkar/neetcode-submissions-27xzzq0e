class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = []
        post = []
        prod = 1
        for num in nums:
            prod = prod * num
            pref.append(prod)
        prod = 1
        for num in nums[ : : -1]:
            prod = prod * num
            post.append(prod)
        ans = []
        for i in range(len(nums)):
            left = pref[i - 1] if i > 0 else 1
            right = post[len(nums) - 2 - i] if i < len(nums) - 1 else 1

            ans.append(left * right)
        return ans