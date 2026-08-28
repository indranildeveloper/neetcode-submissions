class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Time Complexity -> O(n)
        # Space Complexity -> O(n)
        charactersCount = {}
        result = 0

        left = 0

        maxFrequency = 0
        
        for right in range(len(s)):
            charactersCount[s[right]] = 1 + charactersCount.get(s[right], 0)
            maxFrequency = max(maxFrequency, charactersCount[s[right]])

            while (right - left + 1) - maxFrequency > k:
                charactersCount[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)
        
        return result