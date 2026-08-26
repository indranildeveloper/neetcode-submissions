class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Time Complexity -> O(n)
        # Space Complexity -> O(1)

        k = k % len(nums)

        def reverseArray(nums, left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverseArray(nums, 0, len(nums) - 1)
        reverseArray(nums, 0, k - 1)
        reverseArray(nums, k, len(nums) - 1)