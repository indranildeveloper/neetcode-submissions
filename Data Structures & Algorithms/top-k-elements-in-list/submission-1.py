class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Time Complexity -> O(n)
        # Space Complexity -> O(n)
        count = {}
        frequency = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num, count in count.items():
            frequency[count].append(num)

        result = []

        for idx in range(len(frequency) - 1, 0, -1):
            for num in frequency[idx]:
                result.append(num)
                if len(result) == k:
                    return result