class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        crsMap = defaultdict(list)
        output = []
        visited = set()
        cycle = set()

        for crs, pre in prerequisites:
            crsMap[crs].append(pre)

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            
            cycle.add(crs)
            for pre in crsMap[crs]:
                if not dfs(pre):
                    return False
            crsMap[crs] = []
            cycle.remove(crs)
            visited.add(crs)
            return True
        

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True