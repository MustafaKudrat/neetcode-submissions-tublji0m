class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        res = 0
        stack = []
        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                if t == "+":
                    sec = int(stack.pop())
                    fir = int(stack.pop())
                    stack.append(fir+sec)
                elif t == "-":
                    sec = int(stack.pop())
                    fir = int(stack.pop())
                    stack.append(fir-sec)
                elif t == "*":
                    sec = int(stack.pop())
                    fir = int(stack.pop())
                    stack.append(fir*sec)
                else:
                    sec = int(stack.pop())
                    fir = int(stack.pop())
                    stack.append(fir/sec)
        res = stack.pop()
        return int(res)