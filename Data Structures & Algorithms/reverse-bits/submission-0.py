class Solution:
    def reverseBits(self, n: int) -> int:
        #0000000...10101
        #1010100...00000

        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            print(bit)
            res = res | (bit << 31-i)

        return res

