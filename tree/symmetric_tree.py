from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def isMirror(t1: TreeNode, t2: TreeNode) -> bool:
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (
                t1.val == t2.val 
                and isMirror(t1.left, t2.right) 
                and isMirror(t1.right, t2.left)
            )
        
        return isMirror(root.left, root.right)


root = TreeNode(2)
root.left = TreeNode(3)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.right = TreeNode(4)
root.right.left = TreeNode(5)

s = Solution()
res = s.isSymmetric(root)
print(res)
