class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d1 = {}
        for i in range(len(strs)):
            s = ''.join(sorted(strs[i]))
            if s not in d1:
                d1[s] = [strs[i]]
            else:
                d1[s].append(strs[i])
        return list(d1.values())
        