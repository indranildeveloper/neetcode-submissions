class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Time Complexity -> O(n)
        # Space Complexity -> O(1)
        globalMax = nums[0]
        globalMin = nums[0]

        currentMax = 0
        currentMin = 0
        total = 0

        for num in nums:
            currentMax = max(currentMax + num, num)
            currentMin = min(currentMin + num, num)
            total += num
            globalMax = max(globalMax, currentMax)
            globalMin = min(globalMin, currentMin)

        return max(globalMax, total - globalMin) if globalMax > 0 else globalMax