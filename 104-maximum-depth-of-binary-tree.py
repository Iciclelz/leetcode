# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if root == None:
            return 0
        
        if root.right == None and root.left == None:
            return 1
        
        if root.right == None and root.left != None:
            return self.maxDepth(root.left) + 1
        
        if root.right != None and root.left == None:
            return self.maxDepth(root.right) + 1
            
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1