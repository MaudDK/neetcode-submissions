class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}

        for v, e in edges:
            graph[v].append(e)
            graph[e].append(v)

        visted = set()

        def dfs(node):
            if node in visted:
                return
            
            visted.add(node)

            for nei in graph[node]:
                dfs(nei)

        components = 0

        for i in range(n):
            if i in visted:
                continue
            else:
                dfs(i)
                components+=1
        
        return components

        