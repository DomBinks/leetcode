#include <stdbool.h>
#include <stdlib.h>

// Structure for linked list nodes 
struct ListNode {
     int val;
     struct ListNode *next;
 };

// Returns the length of the linked list
int listLength(struct ListNode* head)
{
    struct ListNode* current = head;
    int length = 0;

    while(current != NULL)
    {
        length++;
        current = current->next;
    }

    return length;
}

// Returns the second half of a linked list
struct ListNode* middleNode(struct ListNode* head)
{
    // Finds the length of the list
    int position = listLength(head);
    // Halves the length to find the middle position
    position = position / 2;

    struct ListNode* current = head;

    // Skips over all the nodes before the middle position
    for(int i = 0; i < position; i++)
    {
        current = current->next;
    }

    // Returns the rest of the list
    return current;
}