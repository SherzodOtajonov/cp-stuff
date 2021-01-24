# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, val):
        if not root:
            return False
        if root.val == val:
            return True
        return self.solve(root.left, val) or self.solve(root.right, val)
