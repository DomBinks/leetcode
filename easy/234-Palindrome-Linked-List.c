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
 
// Returns whether the provided linked list is a palindrome
bool isPalindrome(struct ListNode* head)
{
    int length = listLength(head);  // Length of the linked list
    int midpoint = length / 2;  // Midpoint of the linked list

    // Stores all the elements in the first half of the linked list
    // (not including the middle item in an odd length list)
    int *firstHalf = calloc(midpoint, sizeof(int));
    struct ListNode* current = head;
    for(int i = 0; i < midpoint; i++)
    {
        firstHalf[i] = current->val;
        current = current->next;
    }

    // Skips over the middle element if the list is an odd length
    if(length % 2 != 0)
    {
        current = current->next;
    }

    // For all the items in the second half
    for(int i = 0; i < midpoint; i++)
    {
        // If it isn't the same as the corresponding element stored
        // in firstHalf
        if(current->val != firstHalf[midpoint - i - 1])
        {
            free(firstHalf);
            return false;
        }

        current = current->next;
    }

    free(firstHalf);
    return true;
}