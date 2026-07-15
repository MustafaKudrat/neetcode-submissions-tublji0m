class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # time = [3, 4.5, 10, 3]
        combine = []
        for i in range(len(position)):
            combine.append((position[i], speed[i]))
        combine.sort()

        time = []
        for p, s in combine:
            time.append((target - p) / s)
        
        stack = []
        for t in time:
            while stack and t >= stack[-1]:
                stack.pop()
            stack.append(t)
        return len(stack)