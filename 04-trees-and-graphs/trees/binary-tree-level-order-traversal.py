# 102 https://leetcode.com/problems/binary-tree-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    levels = []
    if not root:
        return levels
    
    def helper(node, level):
        if len(levels) == level:
            levels.append([])
            
        levels[level].append(node.val)
        
        if node.left:
            helper(node.left, level+1)
        if node.right:
            helper(node.right, level+1)
    
    helper(root, 0)
    return levels