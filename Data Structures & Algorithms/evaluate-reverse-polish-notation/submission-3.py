class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Time Complexity -> O(n)
        # Space Complexity -> O(n)
        stack = []
        for ch in tokens:
            if ch == "+":
                second_number = stack.pop()
                first_number = stack.pop()
                result = first_number + second_number
                stack.append(result)
            elif ch == "-":
                second_number = stack.pop()
                first_number = stack.pop()
                result = first_number - second_number
                stack.append(result)
            elif ch == "*":
                second_number = stack.pop()
                first_number = stack.pop()
                result = first_number * second_number
                stack.append(result)
            elif ch == "/":
                second_number = stack.pop()
                first_number = stack.pop()
                result = int(first_number / second_number)
                stack.append(result)
            else:
                stack.append(int(ch))
        return stack[0]