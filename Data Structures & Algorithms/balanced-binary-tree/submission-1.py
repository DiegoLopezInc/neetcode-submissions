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
        
            l = 0
            r = 0
            l_balanced = True
            r_balanced = True

            if node.left:
                l_balanced, l = dfs(l_balanced, node.left)
            if node.right:
                r_balanced, r = dfs(r_balanced, node.right)

            if abs(l - r) > 1:
                balance = False
            if l_balanced == False or r_balanced == False:
                balance = False

            return [balance, max(l, r)+ 1]
        
        balance, length = dfs(True, root)
        return balance
