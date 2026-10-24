class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        stack = []

        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif len(stack) != 0:
                if stack[-1] != '(' and c == ')':
                    return False
                if stack[-1] != '{' and c == '}':
                    return False
                if stack[-1] != '[' and c == ']':
                    return False
                stack.pop()
            else:
                return False
        if len(stack) > 0:
            return False
        return True 