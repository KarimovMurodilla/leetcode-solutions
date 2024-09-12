class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    
class Solution:
    def calculate(self, root: TreeNode):
        if not root:
            return 0
        
        max_left_path = self.calculate(root.left)
        max_right_path = self.calculate(root.right)
        return max(max_left_path, max_right_path) + root.val
    

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.right.right = TreeNode(3)
root.left.left.left = TreeNode(4)
root.right.right.right = TreeNode(4)

sol = Solution()
res = sol.calculate(root)
print(res)