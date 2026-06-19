# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, root, visited) -> List[int]:

        if root in visited:
            return []

        if root == None:
            return []

        # get left side vals
        if root.left:
            visited += self.dfs(root.left, [])
        
        # and root val
        visited += [root.val]

        # add right vals
        if root.right:
            visited += self.dfs(root.right, [])
        
        return visited
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        visited = []
        return self.dfs(root,visited)