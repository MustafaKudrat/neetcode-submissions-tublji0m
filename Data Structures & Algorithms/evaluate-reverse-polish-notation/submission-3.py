class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t.isdigit() or len(t) > 1:
                stack.append(int(t))
            else:
                right = stack.pop()
                left = stack.pop()
                val = self.calculate(left, right, t)
                stack.append(val)
        return stack[0]
                
    def calculate(self, left, right, sign):
        if sign == '+':
            return left + right
        elif sign == '-':
            return left - right
        elif sign == '*':
            return left * right
        elif sign == '/':
            return int(left / right)