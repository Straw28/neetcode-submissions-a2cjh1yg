class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = {}
        for i in strs:
            alpha = "".join(sorted(i))
            if alpha in anagramDict:
                anagramDict[alpha].append(i)
            else:
                anagramDict[alpha] = [i]
            
        return list(anagramDict.values())