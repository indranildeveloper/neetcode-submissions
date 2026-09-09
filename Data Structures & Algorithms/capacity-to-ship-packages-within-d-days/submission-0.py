class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Time Complexity -> O(nlog(m))
        # Space Complexity -> O(1)
        left = max(weights)
        right = sum(weights)
        result = right

        while left <= right:
            mid = left + ((right - left) // 2)

            if self.canShip(mid, weights, days):
                result = min(result, mid)
                right = mid - 1
            else:
                left = mid + 1

        return result

    def canShip(self, capacity, weights, days):
        ships = 1
        currentCapacity = capacity
        for weight in weights:
            if currentCapacity - weight < 0:
                ships += 1
                currentCapacity = capacity
            currentCapacity -= weight
        return ships <= days

