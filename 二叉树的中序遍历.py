#二叉树的中序遍历

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []  
        # 中序递归 
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
