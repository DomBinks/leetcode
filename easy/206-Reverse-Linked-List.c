#include <stdlib.h>

struct ListNode
{
    int val;
    struct ListNode *next;
};

// Reverses the linked list pointed to be head
struct ListNode *reverseList(struct ListNode* head)
{
    // Null list case
    if(head == NULL)    
    {
        return head;
    }

    struct ListNode *current = head;
    struct ListNode *next = current->next; 
    current->next = NULL;

    // While there are nodes left to be reversed
    while(next != NULL)
    {
        current = next; // Go the the next node
        next = current->next; // Store the node after the current node

        current->next = head; // Set the current node to point to head
        head = current; // Set the current node to the head 
    }

    // Return the head node 
    return head;
}