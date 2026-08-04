class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        sorted_nums = sorted(count.keys(), key = lambda x : count[x], reverse = True)
        print(sorted_nums)
        return sorted_nums[:k]

        