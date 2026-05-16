class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for i in range(len(strs)):
            str_tuple = tuple(sorted(strs[i]))
            if str_tuple not in anagram_map :
                anagram_map[str_tuple] = [strs[i]]
            else:
                anagram_map[str_tuple] += [strs[i]]
        res = []
        for key, value in anagram_map.items():
            res.append(value)
        return res
