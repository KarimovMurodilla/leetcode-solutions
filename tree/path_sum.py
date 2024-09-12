from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    
class Solution:
    def __init__(self):
        self.sums = []

    def path_sum(self, root: Optional[TreeNode]):
        if not root:
            print(root)
            return 0
        
        max_left_path = self.path_sum(root.left)
        max_right_path = self.path_sum(root.right)
        self.sums.append(max_left_path + root.val)
        self.sums.append(max_right_path + root.val)
        return max(max_left_path, max_right_path) + root.val
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.path_sum(root)
        return targetSum in self.sums
    

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.right.right = TreeNode(3)
root.left.left.left = TreeNode(4)
root.right.right.right = TreeNode(4)

sol = Solution()
res = sol.hasPathSum(root, 10)
print(res)
