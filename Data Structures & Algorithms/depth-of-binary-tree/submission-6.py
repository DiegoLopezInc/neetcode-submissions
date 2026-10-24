# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        
        def dfs(n):
            if n is None:
                return 0

            l = dfs(n.left)
            r = dfs(n.right)

            return max(l,r) + 1

        return dfs(root)

            

