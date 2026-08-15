class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Time Complexity -> O(n)
        # Space Complexity -> O(1)
        left = 0
        right = len(heights) - 1
        maxWater = 0

        while left < right:
            containerWidth = right - left
            containerHeight = min(heights[left], heights[right])
            containerArea = containerWidth * containerHeight
            maxWater = max(maxWater, containerArea)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxWater