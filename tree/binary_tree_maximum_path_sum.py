from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.answer = 0

    def helper(self, root: Optional[TreeNode]):
        if not root:
            return 0
        
        max_left_path = max(self.helper(root.left), 0)
        max_right_path = max(self.helper(root.right), 0)
        self.answer = max(self.answer, max_left_path + max_right_path + root.val)

        return max(max_left_path, max_right_path) + root.val

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root.val and (not root.left and not root.right):
            return root.val
            
        self.helper(root)
        return self.answer


root = TreeNode(1)
root.left = TreeNode(2)
# root.right = TreeNode(2)
# root.left.left = TreeNode(3)
# root.right.right = TreeNode(3)
# root.left.left.left = TreeNode(4)
# root.right.right.right = TreeNode(4)

s = Solution()
res = s.maxPathSum(root)
print(res)
