class TimeMap:
#alice: 1:happy
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        #if key in self.store:
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        l, r = 0, len(self.store[key]) - 1
        while l <= r:
            mid = (l + r) // 2
            if timestamp == self.store[key][mid][0]:
                return self.store[key][mid][1]
            elif self.store[key][mid][0] < timestamp:
                l = mid + 1
            else:
                r = mid - 1
        if r >= 0:
            return self.store[key][r][1]
        else:
            return ""
