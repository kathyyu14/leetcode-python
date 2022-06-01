class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # course map
        preMap = {i:[] for i in range(numCourses)}
        
        # graph course
        for course, pre in prerequisites:
            preMap[course].append(pre)
        
        visiting = set()
        def dfs(crs):
            if crs in visiting:
                return False
        
            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
                    