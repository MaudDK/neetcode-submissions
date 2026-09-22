class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:  
        #If n = 0 , automatically True, its an empty graph
        if n == 0:
            return True
        
        #Build Adjacency List
        graph = defaultdict(list)

        for v, e in edges:
            graph[v].append(e)
            #Also we need to have reverse direction since undirected graph
            graph[e].append(v)
        
        #In order for a graph to be a valid tree
        #1. There must be no cycles, aka not in a visted set already
        #2. The only case that is allowed is if its going back to a previous node

        visted = set()
        def dfs(node, previous):
            #If this node has been visted, cycle detected
            if node in visted:
                return False
            
            visted.add(node) #Visit it
            #Loop through the neighbors
            for nei in graph[node]:
                #If the neighbor is the previous element, its fine skip
                if nei == previous:
                    continue
                #If dfs returns false (node has been visted, cycle detected)
                #Recursive step check neighbor and pass previous node as current
                if not dfs(nei, node):
                    return False
            return True
        
        #If we have not visited all nodes, meaning there is a disconnect
        return dfs(0, -1) and len(visted) == n
                



        