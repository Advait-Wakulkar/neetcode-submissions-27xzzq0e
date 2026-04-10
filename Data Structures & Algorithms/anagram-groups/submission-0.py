class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for i in range(len(strs)):
            sorted_str = tuple(sorted(strs[i]))
            if sorted_str not in seen:
                seen[sorted_str] = [strs[i]]
            else:
                seen[sorted_str].append(strs[i])
        res = []
        for key, value in seen.items():
            res.append(value)
        return res