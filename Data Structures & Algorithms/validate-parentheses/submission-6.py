class Solution:
    def isValid(self, s: str) -> bool:
        pair = {"}": "{", ")": "(", "]": "["}
        stack = []

        for c in s:
            if c in pair:
                if stack: 
                    if stack.pop() != pair[c]:
                        return False
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0