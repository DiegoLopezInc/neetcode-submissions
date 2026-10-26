# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        diameter = 0

        def dfs(node):
            l = 0
            r = 0
            if not node:
                return
            
            nonlocal diameter
            if node.left:
                l = dfs(node.left)
            if node.right:
                r = dfs(node.right)
            if l + r > diameter:
                diameter = l + r
            return max(l, r) + 1
        
        dfs(root)
        return diameter
