class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dS, dT = {}, {}
        for i in s:
            if i not in dS:
                dS[i] = 1
            else:
                dS[i] += 1
        for i in t:
            if i not in dT:
                dT[i] = 1
            else:
                dT[i] += 1
        print(dS, dT)
        return dS == dT        