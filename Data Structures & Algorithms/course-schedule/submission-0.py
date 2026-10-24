class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        # visitSet = all courses along the curr DFS path
        visitSet = set()
        def dfs(c):
            if c in visitSet:
                return False
            if preMap[c] == []:
                return True
            
            visitSet.add(c)
            for pre in preMap[c]:
                if not dfs(pre): return False
            
            visitSet.remove(c)
            preMap[c] = []
            
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
