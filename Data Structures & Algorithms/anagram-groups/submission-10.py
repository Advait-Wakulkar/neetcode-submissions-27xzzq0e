class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupedStrs = {}
        for string in strs:
            cleaned = "".join(sorted(string))
            if cleaned not in groupedStrs:
                groupedStrs[cleaned] = [string]
            else:
                groupedStrs[cleaned].append(string)
        res = [values for values in groupedStrs.values()]
        return res[::-1]