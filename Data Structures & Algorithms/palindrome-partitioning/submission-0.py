class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curList = []

        def bt(i):
            if i >= len(s):
                res.append(curList[:])
                return
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    curList.append(s[i: j + 1])
                    bt(j + 1)
                    curList.pop()

        bt(0)
        return res


    def isPalindrome(self, word, l, r):
        while l <= r:
            if word[l] != word[r]:
                return False
            l += 1
            r -= 1
        return True