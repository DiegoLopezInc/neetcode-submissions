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
            if balance == False: return [False, 0]
        
            l_balanced, l = dfs(balance, node.left)
            r_balanced, r = dfs(balance, node.right) 

            if abs(l - r) > 1:
                balance = False
            if l_balanced == False or r_balanced == False:
                balance = False

            return [balance, max(l, r)+ 1]
        
        balance, length = dfs(True, root)
        return balance
