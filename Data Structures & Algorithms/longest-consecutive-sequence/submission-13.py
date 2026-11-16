class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_count = 0
        for num in nums:
            if num - 1 not in set_nums:
                count = 1
                l = num
                while (l + 1) in set_nums:
                    count += 1
                    l += 1
                max_count = max(max_count, count)
        return max_count
        