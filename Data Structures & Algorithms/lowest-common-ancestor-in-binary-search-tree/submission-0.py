# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None

        if root == p or root == q:
            return root

        if self.isAncestor(root.left, p) and self.isAncestor(root.left, q):
            return self.lowestCommonAncestor(root.left, p, q)

        if self.isAncestor(root.right, p) and self.isAncestor(root.right, q):
            return self.lowestCommonAncestor(root.right, p, q)

        return root
    
    def isAncestor(self, node, target):
            if not node:
                return False
            
            if node.val == target.val:
                return True
            
            left = self.isAncestor(node.left, target)
            right = self.isAncestor(node.right, target)
            
            return left or right

        
                
        