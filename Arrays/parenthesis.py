class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize an empty stack to keep track of opening brackets
        stack = []

        # Iterate through each character in the input string
        for char in s:
            # If the character is an opening bracket, push it onto the stack
            if char in ["(", "{", "["]:
                stack.append(char)
            else:
                # If the stack is empty, it means there's no matching opening bracket
                if len(stack) < 1:
                    return False

                # Check if the top of the stack matches the current closing bracket
                if (
                    (stack[-1] == "(" and char != ")")
                    or (stack[-1] == "{" and char != "}")
                    or (stack[-1] == "[" and char != "]")
                ):
                    return False  # Mismatched brackets

                # If there is a match, pop the opening bracket from the stack
                else:
                    stack.pop()

        # After processing all characters, check if there are any unmatched opening brackets left in the stack
        if len(stack) > 0:
            return False  # There are unmatched opening brackets

        # If all brackets are matched correctly, return True
        return True
