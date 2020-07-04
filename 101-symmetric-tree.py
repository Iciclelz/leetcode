# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isSymmetric_(self, leftBranch, rightBranch):
        
        if leftBranch == None and rightBranch == None:
            return True
        
        if leftBranch == None and rightBranch != None:
            return False
        
        if leftBranch != None and rightBranch == None:
            return False
        
        #print((leftBranch.val, rightBranch.val))
        if leftBranch.val != rightBranch.val:
            return False
        
        return self.isSymmetric_(leftBranch.left, rightBranch.right) and self.isSymmetric_(rightBranch.left, leftBranch.right)
    
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if root == None:
            return True
        
        return self.isSymmetric_(root.left, root.right)
        
        