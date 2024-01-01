# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Just list2 if no list1
        if list1 == None:
            return list2

        # Just list1 if no list2
        if list2 == None:
            return list1

        l1 = list1 # Current position in list1
        l2 = list2 # Current position in list2

        # Get the starting node and advance the position in
        # the list it's from
        if l1.val < l2.val:
            ptr = l1
            l1 = l1.next
        else:
            ptr = l2
            l2 = l2.next
        
        head = ptr # Cache the head of the list

        # While there is a choice of which list to pick from
        while l1 and l2:
            # If the current position in list1 is smaller
            if l1.val < l2.val:
                ptr.next = l1 # Set the next node in the list
                ptr = ptr.next # Update the last node in the list
                l1 = l1.next # Go to the next node in list1

            # If the current position in list2 is smaller
            else:
                ptr.next = l2 # Set the next node in the list
                ptr = ptr.next # Update the last node in the list
                l2 = l2.next # Go to the next node in list2

        # Only nodes in list1 left
        if l1:
            # Add them to the end
            ptr.next = l1 
        
        # Only nodes in list2 left
        if l2:
            # Add them to the end
            ptr.next = l2

        return head # Return the cached head
