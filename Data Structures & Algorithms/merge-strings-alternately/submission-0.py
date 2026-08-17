class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Time Complexity -> O(n)
        # Space Complexity -> O(n)
        word1Pointer = 0
        word2Pointer = 0

        result = ""

        while word1Pointer < len(word1) and word2Pointer < len(word2):
            result += word1[word1Pointer]
            result += word2[word2Pointer]

            word1Pointer += 1
            word2Pointer += 1

        if word1Pointer < len(word1):
            result += word1[word1Pointer:]
        
        if word2Pointer < len(word2):
            result += word2[word2Pointer:]

        return result
        