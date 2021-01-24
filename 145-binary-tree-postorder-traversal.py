# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree_traversal(self, algorithm, node):
        if node == None:
            return None
        
        values = list()
        if algorithm == 'preorder':
            values.append(node.val)
            
        if node.left != None:
            values += self.tree_traversal(algorithm, node.left)
        
        if algorithm == 'inorder':
            values.append(node.val)
        
        if node.right != None:
            values += self.tree_traversal(algorithm, node.right)
        
        if algorithm == 'postorder':
            values.append(node.val)
            
        return values
    
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        return self.tree_traversal('postorder', root)