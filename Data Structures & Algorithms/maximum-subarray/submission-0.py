class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Time Complexity -> O(n)
        # Space Complexity -> O(1)

        currentSum = 0
        maxSum = float("-inf")

        for num in nums:
            currentSum += num
            maxSum = max(maxSum, currentSum)

            if currentSum < 0:
                currentSum = 0
        
        return maxSum
