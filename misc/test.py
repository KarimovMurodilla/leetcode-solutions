from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root: TreeNode):
            if not root:
                return False
            
            left = helper(root.left)
            right = helper(root.right)

            if left == -1 or right == -1:
                return -1
            
            if abs(left - right) > 1:
                return -1
            
            return max(left, right) + 1
        
        return helper(root) != -1
        

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
# root.left.left = TreeNode(3)
# root.right.right = TreeNode(3)
# root.left.left.left = TreeNode(4)
# root.right.right.right = TreeNode(4)

s = Solution()
res = s.isBalanced(root)
print(res)
