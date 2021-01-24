# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
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
                
                child_depth = depth + 1
                if node.left != None and node.left not in explored:
                    queue.append((node.left, child_depth))
                    if depth + 1 in result:
                        result[child_depth].append(node.left.val)
                    else:
                        result[child_depth] = [node.left.val]
                
                if node.right != None and node.right not in explored:
                    queue.append((node.right, child_depth))
                    if depth + 1 in result:
                        result[child_depth].append(node.right.val)
                    else:
                        result[child_depth] = [node.right.val]
                    
        return list(result.values())