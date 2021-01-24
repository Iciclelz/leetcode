"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def tree_traversal(self, algorithm, node):
        if node == None:
            return
        
        values = list()
        if algorithm == 'preorder':
            values.append(node.val)
            
        for child in node.children:
            values += self.tree_traversal(algorithm, child)
        
        if algorithm == 'postorder':
            values.append(node.val)
        return values
        
        
    def postorder(self, root: 'Node') -> List[int]:
        return self.tree_traversal('postorder', root)