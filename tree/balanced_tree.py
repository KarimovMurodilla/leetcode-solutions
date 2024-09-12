from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: TreeNode):
            if not root: return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]

    def isBalanced2(self, root: TreeNode) -> bool:
        # Вспомогательная функция для расчета высоты поддерева
        def check_height(node):
            if not node:
                return 0  # Пустое дерево имеет высоту 0

            # Рекурсивно находим высоту левого и правого поддеревьев
            left_height = check_height(node.left)
            right_height = check_height(node.right)
        
            # Если любое поддерево несбалансировано, возвращаем -1
            if left_height == -1 or right_height == -1:
                return -1
            
            # Если разница в высотах поддеревьев больше 1, то дерево несбалансировано
            if abs(left_height - right_height) > 1:
                return -1
            
            # Возвращаем высоту поддерева
            return max(left_height, right_height) + 1

        # Если вспомогательная функция возвращает -1, то дерево несбалансировано
        return check_height(root) != -1
        

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.right.right = TreeNode(3)
root.left.left.left = TreeNode(4)
root.right.right.right = TreeNode(4)

s = Solution()
res = s.isBalanced2(root)
print(res)
