# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs_path(root, targetSum, current_sum)->bool:
            
            # when passed nothing
            if root == None:
                print("root is none")
                return False

            # increase sum based on root val
            current_sum = root.val + current_sum
            print(current_sum)

            # is a leaf node if left and right is None
            if (root.left == None) and (root.right == None):
                return targetSum == current_sum
            else:
                # if left or right equals target, then true
                left_equals_target = dfs_path(root.left, targetSum, current_sum)
                right_equals_target = dfs_path(root.right, targetSum, current_sum)
                return left_equals_target or right_equals_target

        return dfs_path(root, targetSum, 0)
        