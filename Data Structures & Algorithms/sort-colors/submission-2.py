class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1

        i = 0

        def swap(left, right):
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp

        while i <= right:
            if nums[i] == 0:
                swap(left, i)
                left += 1
            elif nums[i] == 2:
                swap(i, right)
                right -= 1
                i -= 1
            i += 1