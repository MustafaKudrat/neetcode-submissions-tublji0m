class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # time = [3, 4.5, 10, 3]
        combine = [(p, s) for p, s in zip(position, speed)]
        combine.sort()
        
        stack = []
        for p, s in combine:
            t = (target - p) / s
            while stack and t >= stack[-1]:
                stack.pop()
            stack.append(t)
        return len(stack)