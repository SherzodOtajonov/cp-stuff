# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, target):
        if not root: return False

        if root.val == target:
            return True
        
        if self.solve(root.left, target): return True
        if self.solve(root.right, target): return True
        return False

def ifNodeExists(node, key):

    res2 = ifNodeExists(node.right, key) 
 
 
