class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        get counter for t
        vars: l, have, need, counter, window, minLen
        for r in len(s)
            add r to window
            update have
            while have == need:
                if curLen < minLen:
                    update minLen
                    update res if len is smaller
                remove window[s[l]]
                update have
                increase l
        return res
        '''

        res = ""
        if t == "":
            return res
        l = 0
        window = defaultdict(int)
        count = Counter(t)
        need = len(count)
        have = 0
        minLen = float('inf')

        for r in range(len(s)):
            window[s[r]] += 1
            if window[s[r]] == count[s[r]]:
                have += 1
            
            while have == need:
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    res = s[l:r + 1]
                
                window[s[l]] -= 1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1

                l += 1
        
        return res











