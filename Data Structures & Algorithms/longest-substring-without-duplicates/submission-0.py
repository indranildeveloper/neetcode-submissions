class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time Complexity -> O(n)
        # Space Complexity -> O(1)
        charactersSet = set()
        left = 0
        result = 0

        for right in range(len(s)):
            while s[right] in charactersSet:
                charactersSet.remove(s[left])
                left += 1
            charactersSet.add(s[right])
            result = max(result, right - left + 1)
        
        return result
