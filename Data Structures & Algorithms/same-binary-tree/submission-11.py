# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]

        while stack:
            nodeA, nodeB = stack.pop()

            if not nodeA and not nodeB:
                continue
            
            if not nodeA or not nodeB or nodeA.val != nodeB.val:
                return False
            
            stack.append((nodeA.left, nodeB.left))
            stack.append((nodeA.right, nodeB.right))
        
        return True
