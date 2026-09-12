# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        q.append(root)

        while q:
            lvl = len(q)
            subarray = list()
            for _ in range(lvl):
                node = q.popleft()

                if node:
                    subarray.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if subarray:
                res.append(subarray)

        return res
            

        