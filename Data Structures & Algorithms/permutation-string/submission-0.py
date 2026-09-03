class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Freq = defaultdict(int)
        for c in s1:
            s1Freq[c] += 1

        s2Freq = defaultdict(int)
        l = 0
        for r in range(len(s2)):
            s2Freq[s2[r]] += 1

            # window too big? shrink from the left
            if r - l + 1 > len(s1):
                s2Freq[s2[l]] -= 1
                if s2Freq[s2[l]] == 0:
                    del s2Freq[s2[l]]   # keep the dicts comparable
                l += 1

            # window is exactly the right size — compare
            if r - l + 1 == len(s1) and s2Freq == s1Freq:
                return True

        return False