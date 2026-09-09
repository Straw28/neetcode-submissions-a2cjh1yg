class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestSq = 0
        setNums = set(nums)
      
    #start of a seq --> num - 1 not in set
        for i in setNums:
            if i-1 not in setNums:
                current = 1
                while i + current in setNums:
                    current += 1
                longestSq = max(longestSq, current)

        return longestSq                
            