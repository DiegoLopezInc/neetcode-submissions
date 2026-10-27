# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        def dfs(balance: bool, node):
            if not node: return [True, 0]
        
            l = dfs(balance, node.left)
            r = dfs(balance, node.right) 

            balance = l[0] and r[0] and abs(l[1] - r[1]) <= 1

            return [balance, max(l[1], r[1]) + 1]
        
        return dfs(True, root)[0]
