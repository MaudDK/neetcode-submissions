class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        visted = set()
        
        def dfs(node):
            if node in visted:
                return False
            
            if graph[node] == []:
                return True
            
            visted.add(node)

            for nei in graph[node]:
                if not dfs(nei):
                    return False
            
            visted.remove(node)
            graph[node] = []
            
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
            




        

        