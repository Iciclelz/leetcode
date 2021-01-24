# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        # bfs
        q = list()
        if root == None:
            return q
        
        result = dict()
        explored = set()
        
        q.append((root, 0))
        result[0] = [root.val]

        while len(q) > 0:
            node, depth = q.pop(0)
            if node not in explored:
                explored.add(node)
                
                child_depth = depth + 1
                if node.left != None and node.left not in explored:
                    q.append((node.left, child_depth))
                    if depth + 1 in result:
                        result[child_depth].append(node.left.val)
                    else:
                        result[child_depth] = [node.left.val]
                
                if node.right != None and node.right not in explored:
                    q.append((node.right, child_depth))
                    if depth + 1 in result:
                        result[child_depth].append(node.right.val)
                    else:
                        result[child_depth] = [node.right.val]
                    
        return reversed(list(result.values()))