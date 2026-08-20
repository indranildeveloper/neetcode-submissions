class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Time Complexity -> O(n^2)
        # Space Complecity -> O(1)
        result = []
        nums.sort()
        target = 0

        for idx, val in enumerate(nums):
            if idx > 0 and val == nums[idx-1]:
                continue
            left = idx + 1
            right = len(nums) - 1

            while left < right:
                currentSum = val + nums[left] + nums[right]

                if currentSum > target:
                    right -= 1
                elif currentSum < target:
                    left += 1
                else:
                    result.append([val, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return result