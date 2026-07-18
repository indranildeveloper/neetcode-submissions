class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers_hash_set = set()

        for num in nums:
            if num in numbers_hash_set:
                return True
            else:
                numbers_hash_set.add(num)
        
        return False