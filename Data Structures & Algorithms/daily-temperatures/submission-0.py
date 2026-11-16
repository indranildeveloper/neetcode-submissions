class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Time Complexity -> O(n)
        # Space Complexity -> O(n)
        result = [0] * len(temperatures)
        stack = []

        for idx, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                stackTemp, stackIdx = stack.pop()
                result[stackIdx] = (idx - stackIdx)
            stack.append((temperature, idx))
        
        return result