class Solution:
    def mySqrt(self, x: int) -> int:
        # Time Complexity -> O(log(n))
        # Space Complexity -> O(1)
        left = 0
        right = x
        result = 0

        while left <= right:
            mid = left + ((right - left) // 2)

            if mid * mid > x:
                right = mid - 1
            elif mid * mid < x:
                left = mid + 1
                result = mid
            else:
                return mid
        
        return result