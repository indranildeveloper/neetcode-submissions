class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Time Complexity -> O(n)
        # Space Complexity -> O(1)
        maxSum = nums[0]
        currentSum = 0

        for idx, num in enumerate(nums):
            currentSum = max(currentSum, 0)
            currentSum += num

            maxSum = max(maxSum, currentSum)

        return maxSum