class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Time Complexity -> O(n^3)
        # Space Complexity -> O(1)
        nums.sort()

        result = []
        quad = []

        def kSum(k, start, target):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    quad.append(nums[i])
                    kSum(k - 1, i + 1, target - nums[i])
                    quad.pop()
                return
            left = start
            right = len(nums) - 1

            while left < right:
                currentSum = nums[left] + nums[right]
                if currentSum < target:
                    left += 1
                elif currentSum > target:
                    right -= 1
                else:
                    result.append(quad + [nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        kSum(4, 0, target)
        return result
