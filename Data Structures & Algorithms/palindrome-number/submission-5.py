class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
        11211
        11211
        get last:
            num % 10 give last
        get first:
            div = 1
            while x >= 10 * div:
                div *= 10
        while x:
            l = x // div
            r = x % 10
            if l != r:
                return False
            x %= div
                x = 1211
            x %= 10
                x = 121
            div was 10000
            div /= 100
                div = 100
        return True
        '''
        if x < 0:
            return False
        div = 1
        while x >= div * 10:
            div *= 10
        # 10000
        while x:
            l = x // div # 232 // 100 = 2 3//1 = 3
            r = x % 10   # 1 232 % 10 = 2 3%10 = 3
            if l != r:
                return False
            x = x % div  # 2321 232 % 100 = 32
            x = x // 10   # 232  32 % 10 = 3
            div //= 100   # 100  1
        return True

