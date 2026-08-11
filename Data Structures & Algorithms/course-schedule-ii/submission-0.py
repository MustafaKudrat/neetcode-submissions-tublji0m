class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        crsMap = defaultdict(list)
        output = []
        visited, cycle = set(), set()

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
            visited.add(crs)
            cycle.remove(crs)
            output.append(crs)
            return True
        

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return output