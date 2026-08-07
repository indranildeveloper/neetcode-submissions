class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Time Complexity -> O(n)
        # Space Complexity -> O(1)
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

            if len(count) <= 2:
                continue
            
            newCount = defaultdict(int)
            for n, c in count.items():
                count[n] -= 1
                if c > 1:
                    newCount[n] = c - 1

            count = newCount
        
        result = []
        for n in count:
            if nums.count(n) > len(nums) // 3:
                result.append(n)
        
        return result


        
