class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = []
        for i in range(n - 1):
            ans.append(max(arr[i + 1 : n]))
        ans.append(-1)
        return ans


        