"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:     
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        self.level(root, 1, res)
        return res
        
    def level(self, root, depth, res):
        if root == None:
            return []
        if len(res) < depth:
            res.append([])
        res[depth - 1].append(root.val)
        # handle children
        for node in root.children:
            self.level(node, depth + 1, res)