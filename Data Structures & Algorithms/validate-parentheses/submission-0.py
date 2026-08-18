class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {")":"(", "]": "[", "}": "{"}

        for r in s:
            if r in valid:
                if stack and stack[-1] == valid[r]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(r)
        
        return True if not stack else False
