# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # Start with the values for level 1 i.e. just the root
        level = 1
        total = root.val

        # Set up the next level
        current = 2
        nodes = self.getInNextLevel([root])

        # While there is another level to look at
        while(nodes != []):
            # Get the sum of all the nodes' values
            here = 0
            for node in nodes:
                here += node.val

            # If this sum is the best so far
            if here > total:
                # Update total to the new max sum
                total = here
                # Update level to this level
                level = current

            # Set up the next level
            current += 1
            nodes = self.getInNextLevel(nodes)

        # Return the level with the highest total sum of node values
        return level

    
    # Take a list of nodes and find all the nodes at the next level
    # i.e. all their children
    def getInNextLevel(self, prev: [TreeNode]) -> [TreeNode]:
        # Stores the nodes in the next level
        nodes = []
        
        # For each node in the previous layer
        for node in prev:
            # If it has a left child
            if node.left:
                # Add the left child to the list
                nodes.append(node.left)
            
            # If it has a right child
            if node.right:
                # Add the right child to the list
                nodes.append(node.right)

        # Return the list of nodes in the next level
        return nodes
