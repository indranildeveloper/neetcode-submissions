class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Time Complexity -> O(nlog(n))
        # Space Complexity -> O(n)
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []
        for p, s in sorted(pair)[::-1]:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)