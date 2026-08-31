class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numset = set(nums)


        #sequence start means there's no number to the left of it
        for i in numset:
            if i - 1 not in numset:
                length = 1
                while (i + length) in numset:
                    length += 1
                longest = max(length, longest)
            
        return longest


            
        