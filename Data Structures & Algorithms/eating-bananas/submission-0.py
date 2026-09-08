class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Time Complexity -> O(nlog(n))
        # Space Complexity -> O(1)
        left = 1
        right = max(piles)
        result = right

        while left <= right:
            mid = left + ((right - left) // 2)
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)

            if hours <= h:
                result = min(result, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return result