# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        current = root # Current node being looked at

        # Find the parent node (current will be the parent)
        while current and (current.left or current.right):
            # If there is a left child and the parent is greater
            if current.left and val < current.val:
                # Go to the left child
                current = current.left

            # If there is a right child and the parent is smaller
            elif current.right and val > current.val:
                current = current.right

            # If there isn't an appropriate child node to go to
            else:
                break

        # If there is no root
        if not root:
            # Set create a new root with the value
            root = TreeNode(val)

        # If the value is less then create a left child
        elif val < current.val:
            current.left = TreeNode(val)

        # If the value is greater then create a right child
        elif val > current.val:
            current.right = TreeNode(val) 

        return root
