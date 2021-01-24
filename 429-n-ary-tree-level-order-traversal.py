"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        # bfs
        queue = list()
        if root == None:
            return queue
        
        result = dict()
        explored = set()
        
        queue.append((root, 0))
        result[0] = [root.val]

        while len(queue) > 0:
            node, depth = queue.pop(0)
            if node not in explored:
                explored.add(node)
           
                for child in node.children:
                    if child not in explored:
                        child_depth = depth + 1
                        queue.append((child, child_depth))
                        if child_depth in result:
                            result[child_depth].append(child.val)
                        else:
                            result[child_depth] = [child.val]

        return list(result.values())