class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Time Complexity -> O(nlon(n))
        # Space Complexity -> O(1)
        people.sort()

        result = 0
        left = 0
        right = len(people) - 1

        while left <= right:
            remainingWeight = limit - people[right]
            right -= 1
            result += 1
            if left <= right and remainingWeight >= people[left]:
                left += 1

        return result
