class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Time Complexity -> O(n)
        # Space Complexity -> O(1)
        result = 0
        count = 0

        for num in nums:
            if count == 0:
                result = num

            count += (1 if num == result else -1)

        return result
