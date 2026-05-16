class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        for i in range(len(nums)):
            if nums[i] not in count_map:
                count_map[nums[i]] = 1
            else:
                count_map[nums[i]] += 1
        sorted_items = sorted(count_map, key=count_map.get, reverse=True)
        return sorted_items[:k]

        