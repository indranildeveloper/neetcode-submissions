class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        result = 0
        max_count = 0

        for num in nums:
            count[num] = 1 + count.get(num, 0)

            if count[num] > max_count:
                result = num
            max_count = max(count[num], max_count)

        return result