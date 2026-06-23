# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        visited = []

        # dfs with a list of values, once len of values is equal to k, return the last value
        def dfs(root,k,visited):

            if len(visited) == k:
                return

            if root.left:
                dfs(root.left,k,visited)
            
            visited.append(root.val)

            if root.right:
                dfs(root.right,k,visited)
        
        dfs(root,k,visited)
        print(visited)
        return visited[k-1]
            

            