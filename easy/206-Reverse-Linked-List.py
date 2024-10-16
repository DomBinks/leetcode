# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        current = head # The current node
        prev = None # The previous nodes

        # While there is another node to go to
        while current.next: 
            nxt = current.next # Cache the next node
            current.next = prev # Set this node's next node to the previous node
            prev = current # Set the previous node to this node
            current = nxt # Set this node to the cached next node

        current.next = prev # Link last node to the rest of the nodes

        return current # Return the last node (stored in current)
