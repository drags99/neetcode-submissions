# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from copy import copy

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # just need height of left and right subtree
        # run dfs on left and right side of root
        def h_dfs(root: Optional[TreeNode]) -> int:
            if root == None:
                return 0
            if root.left or root.right:
                return 1 + max(h_dfs(root.left),h_dfs(root.right))
            return 0

        def check_balance(root):
            if root == None:
                return True
            l = copy(root)
            r = copy(root)
            l.right = None
            r.left = None
            if abs(h_dfs(l) - h_dfs(r)) > 1:
                return False
            else:
                print(f"l:{h_dfs(l)} r:{h_dfs(r)}")
                return check_balance(root.left) and check_balance(root.right)

        # when root is empty, is balanced
        return check_balance(root)
        