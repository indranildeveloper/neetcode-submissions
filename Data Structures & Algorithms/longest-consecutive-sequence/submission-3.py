class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Time Complexity -> O(n)
        # Space Complexity -> O(n)
        numsSet = set(nums)
        longestSequence = 0

        for num in numsSet:
            if (num - 1) not in numsSet:
                length = 0
                while (num + length) in numsSet:
                    length += 1
                longestSequence = max(length, longestSequence)
        
        return longestSequence

        