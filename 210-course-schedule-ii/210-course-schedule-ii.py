class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # adj map
        preMap = { i:[] for i in range(numCourses)}
        for crs, prev in prerequisites:
            preMap[crs].append(prev)
        
        res = []
        visit, circle = set(), set()
        
        def dfs(crs):
            if crs in circle:
                return False
            
            if crs in visit:
                return True
            
            circle.add(crs)
            for prev in preMap[crs]:
                if dfs(prev) == False:
                    return False
            circle.remove(crs)
            visit.add(crs)
            res.append(crs)
            
            return True
            
            
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return res
            
            
        
        
        