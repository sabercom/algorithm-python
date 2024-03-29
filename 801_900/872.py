# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(node):
            if not node.left and not node.right:
                yield node.val
            if node.left:
                yield from dfs(node.left)
            if node.right:
                yield from dfs(node.right)

        return tuple(dfs(root1)) == tuple(dfs(root2))
