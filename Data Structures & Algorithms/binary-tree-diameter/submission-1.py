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
        max_subtree = 0

        def dfs(node):
            nonlocal max_subtree
            l = 0
            r = 0
            if not node:
                return 0
            if node.left:
                l = dfs(node.left)
            if node.right:
                r = dfs(node.right)
            if l + r > max_subtree:
                max_subtree = l + r
            return max(l, r) + 1
        
        dfs(root)
        return max_subtree
        