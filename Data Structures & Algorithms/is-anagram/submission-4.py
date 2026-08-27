class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sDict, tDict = defaultdict(int), defaultdict(int)

        for i in range(len(s)):
            sChar = s[i]
            tChar = t[i]
            sDict[sChar] += 1
            tDict[tChar] += 1

        return sDict == tDict
        