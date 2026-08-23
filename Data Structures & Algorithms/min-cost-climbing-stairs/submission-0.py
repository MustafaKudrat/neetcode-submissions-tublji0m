class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        res = 0

        cost1, cost2 = cost[-2], cost[-1]

        for i in range(len(cost) - 3, -1, -1):
            tmp = cost1
            cost1 = cost[i] + min(cost1, cost2)
            cost2 = tmp

        return min(cost1, cost2)