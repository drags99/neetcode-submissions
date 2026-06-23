"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def R(root):
            if root:
                if root.left == None:
                    return
                if root.left:
                    root.left.next = root.right
                if root.next:
                    bridge_node = root.next.left
                    root.right.next = bridge_node
                R(root.left)
                R(root.right)
            return

        R(root)
        return root