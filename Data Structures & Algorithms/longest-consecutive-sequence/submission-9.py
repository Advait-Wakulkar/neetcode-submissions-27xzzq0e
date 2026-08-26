class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setOfNums = set(nums)
        maxCount = 0
        for num in setOfNums:
            if (num - 1) not in setOfNums:
                count = 1
                while(num + count) in setOfNums:
                    count += 1
                maxCount = max(maxCount, count)
        return maxCount
