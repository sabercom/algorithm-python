# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original:
            return None
        if original.val == target.val:
            return cloned
        if left := self.getTargetCopy(original.left, cloned.left, target):
            return left
        if right := self.getTargetCopy(original.right, cloned.right, target):
            return right
