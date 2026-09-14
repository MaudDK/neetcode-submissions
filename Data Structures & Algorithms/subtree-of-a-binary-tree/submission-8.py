# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True

        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        
        return left or right


    
    def isSameTree(self, tree_a, tree_b) -> bool:
        if not tree_a and not tree_b:
            return True
        
        if not tree_a or not tree_b or tree_a.val != tree_b.val:
            return False
        
        left = self.isSameTree(tree_a.left, tree_b.left)
        right = self.isSameTree(tree_a.right, tree_b.right)

        return left and right


        
        
