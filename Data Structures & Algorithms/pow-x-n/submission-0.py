class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Time Complexity -> O(nlog(n))
        # Space Complexity -> O(1)
        def helper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1

            result = helper(x, n // 2)
            result = result * result
            return x * result if n % 2 else result

        result = helper(x, abs(n))
        return result if n >= 0 else 1 / result