from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.sums = []

    def hasPathSum(self, root: Optional[TreeNode], target: int):
        if not root:
            return False
        
        target -= root.val

        # Leaf of the tree
        if not root.left and not root.right:
            return target == 0
        
        return (self.hasPathSum(root.left, target) or self.hasPathSum(root.right, target))
    

root = TreeNode(1)
root.left = TreeNode(2)
# # root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.left.right = TreeNode(4)

# root.right.right = TreeNode(3)
# root.left.left.left = TreeNode(4)
# root.right.right.right = TreeNode(8)

sol = Solution()
res = sol.hasPathSum(root, 10)
print(res)
