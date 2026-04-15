class Solution:
    def calculate(self, s: str) -> int:
        s += '+'  # sentinel to flush the last number
        res = 0
        last = 0
        num = 0
        op = '+'

        for ch in s:
            if ch.isdigit():
                num = num * 10 + (ord(ch) - 48)
            elif ch == ' ':
                continue
            else:
                if op == '+':
                    res += last
                    last = num
                elif op == '-':
                    res += last
                    last = -num
                elif op == '*':
                    last = last * num
                elif op == '/':
                    # truncate toward zero
                    last = int(last / num)

                op = ch
                num = 0

        return res + last
