class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Time Complexity -> O(n)
        # Space Complexity -> O(1)

        left = 0
        right = len(numbers) - 1

        while left < right:
            currentSum = numbers[left] + numbers[right]

            if currentSum < target:
                left += 1
            elif currentSum > target:
                right -= 1
            else:
                return [left + 1, right + 1]
        
        return []