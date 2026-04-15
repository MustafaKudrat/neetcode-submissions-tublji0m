class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # first find how long it takes for each car to get to destination
        timeStack = []
        pair = [ (p,s) for p, s in zip(position, speed)]
        pair.sort(reverse = True)

        for p, s in pair:
            timeStack.append((target-p)/s)
            while len(timeStack) >= 2 and timeStack[-1] <= timeStack[-2]:
                timeStack.pop()


        return len(timeStack) 