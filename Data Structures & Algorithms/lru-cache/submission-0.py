from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.q = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.q:
            self.q.move_to_end(key)
            return self.q[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.q:
            self.q.move_to_end(key)
            self.q[key] = value
        else:
            self.q[key] = value
            if len(self.q) > self.cap:
                self.q.popitem(last=False)
