from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(node):
            if not node:
                return
            ans.append(node.val)  # Visit the root
            preorder(node.left)   # Traverse left subtree
            preorder(node.right)  # Traverse right subtree
        
        ans = []
        preorder(root)
        return ans
