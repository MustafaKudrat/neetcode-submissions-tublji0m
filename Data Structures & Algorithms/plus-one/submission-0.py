class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        i = len(digits) - 1
        res = []
        while i >= 0 or carry:
            if i == len(digits) - 1:
                summ = digits[i] + 1 + carry
            else:
                if i < 0:
                    summ = carry
                else:
                    summ = digits[i] + carry
            res.append(summ % 10)
            carry = summ // 10
            i -= 1
        return res[::-1]