# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set() # Store seen nodes

        current = head # Current node

        # While there is another node to look at
        while(current != None):
            if current in seen:
                # Return True as there is a cycle as this node has
                # been seen before
                return True
            else:
                # Add this node to the seen set
                seen.add(current)
                # Get the next node
                current = current.next

        # No cycles found so return False
        return False
        
