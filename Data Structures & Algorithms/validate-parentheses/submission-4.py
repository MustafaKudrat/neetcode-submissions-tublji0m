class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []
        for p in s:
            if p in pairs:
                if stack and stack.pop() == pairs[p]:
                    continue
                else:
                    return False
            else:
                stack.append(p)
        return len(stack) == 0