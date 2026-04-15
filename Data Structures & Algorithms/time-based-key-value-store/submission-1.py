class TimeMap:

    def __init__(self):
        self.dict = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.dict[key]) - 1
        val = self.dict[key]

        res = ""

        while l <= r:
            m = (l + r) // 2
            if val[m][0] <= timestamp:
                res = val[m][1]
                l = m + 1
            else:
                r = m - 1

        return res
        