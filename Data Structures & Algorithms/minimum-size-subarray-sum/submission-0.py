class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Time Complexity -> O(n)
        # Space Complexity -> O(1)
        left = 0
        currentTotal = 0

        minLength = float("inf")

        for right in range(len(nums)):
            currentTotal += nums[right]

            while currentTotal >= target:
                minLength = min(minLength, right - left + 1)
                currentTotal -= nums[left]
                left += 1

        return 0 if minLength == float("inf") else minLength