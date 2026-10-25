# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.dfs(root)
        
    def dfs(self, node):
        l = 0
        r = 0
        if not node:
            return 0
        if node.left:
            l = self.dfs(node.left)
        if node.right:
            r = self.dfs(node.right)
        return max(l, r) + 1
        