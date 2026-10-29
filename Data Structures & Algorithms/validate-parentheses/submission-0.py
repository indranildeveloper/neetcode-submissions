class Solution:
    def isValid(self, s: str) -> bool:
        # Time Complexity -> O(n)
        # Space Complexity -> O(n)
        openingBrackets = "({["
        closingBrackets = ")}]"
        matchingBrackets = {")": "(", "}": "{", "]": "["}

        stack = []

        for char in s:
            if char in openingBrackets:
                stack.append(char)
            elif char in closingBrackets:
                if len(stack) == 0:
                    return False
                elif stack[-1] == matchingBrackets[char]:
                    stack.pop()
                else:
                    return False
            
        return len(stack) == 0