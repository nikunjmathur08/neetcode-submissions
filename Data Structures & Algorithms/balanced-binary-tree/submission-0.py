# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def get_height(node):
            if not node:
                return 0
            
            left_height = get_height(node.left)
            right_height = get_height(node.right)

            if left_height == -1 or right_height == -1:
                return -1
            
            if abs(left_height - right_height) > 1:
                return -1

            return max(left_height, right_height) + 1
        
        diff = get_height(root)
        if diff == -1:
            return False
        
        return True