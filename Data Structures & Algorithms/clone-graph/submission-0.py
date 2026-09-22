"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        clones = {}
        clones[node] = Node(node.val)
        queue = deque()
        queue.append(node)

        while queue:
            current = queue.popleft()
            for nei in current.neighbors:
                if nei not in clones:
                    copy = Node(nei.val)
                    clones[current].neighbors.append(copy)
                    queue.append(nei)
                    clones[nei] = copy
                else:
                    clones[current].neighbors.append(clones[nei])
        
        return clones[node]


                    


        

        
        
        