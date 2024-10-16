# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        vals = self.getVals(root) # Get all the values of nodes in the tree
        vals.sort() # Sort the list of values
        
        minimum = 10**5 + 1 # Set to a large integer
        for i in range(len(vals) - 1): # For each value up to the penultimate value
            # If the difference between this node and the next node is the smallest yet
            if vals[i+1] - vals[i] < minimum:
                # Update minimum
                minimum = vals[i+1] - vals[i]

        return minimum
    
    # Get the values of all the nodes using a DFS
    def getVals(self, root: Optional[TreeNode]) -> [int]:
        # Add the root node's value to the list
        out = [root.val]
        # Get the values of all children in the left subtree
        if root.left:
            out += self.getVals(root.left)
        # Get the values of all children in the right subtree
        if root.right:
            out += self.getVals(root.right)
        
        # Return the list of values
        return out
