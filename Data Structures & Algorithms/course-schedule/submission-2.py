class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map course to preReq
        preReq = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preReq[crs].append(pre)

        visited = set()

        # dfs
         # return True if no cycle, no preReq, or preReq is met
         # return False if cycle
        def dfs(crs):
            if preReq[crs] == []:
                return True
            if crs in visited:
                return False

            visited.add(crs)
            for pre in preReq[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            preReq[crs] = []
            return True


        # call dfs on any node to start
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

