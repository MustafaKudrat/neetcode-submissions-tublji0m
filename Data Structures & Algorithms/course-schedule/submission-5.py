class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = defaultdict(list)
        for crs, preReq in prerequisites:
            courseMap[crs].append(preReq)

        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if courseMap[crs] == []:
                return True
            visited.add(crs)
            for preReq in courseMap[crs]:
                if not dfs(preReq):
                    return False
            visited.remove(crs)
            courseMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True