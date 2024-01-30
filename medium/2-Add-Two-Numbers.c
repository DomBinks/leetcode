#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

// Adds two numbers together provided as linked lists of digits in
// reverse order, returning the answer as a linked list in reverse
// order
struct ListNode* addTwoNumbers(struct ListNode* l1, \
    struct ListNode* l2){
    // Track the current element being looked at from the input lists
    struct ListNode* elem1 = l1;
    struct ListNode* elem2 = l2;

    // Store the first, penultimate, and last node
    // Allocating memory for the first node
    struct ListNode* start = calloc(1, sizeof(struct ListNode));
    struct ListNode* prev;
    struct ListNode* end = start;

    // While there is a node left in both lists
    while(elem1 != NULL && elem2 != NULL)
    {
        int sum = elem1->val + elem2->val; // Find the sum
        if(end->val > 9)
        {
            sum++; // Add 1 if there is a carry
        }

        // Allocate memory for the next node in the answer list
        end->next = calloc(1, sizeof(struct ListNode));
        if(sum > 9) // If there is a carry
        {
            // Decrease the sum by 10, leaving just the single lower
            // digit
            end->val = sum - 10;
            // Set the value of the next node to > 9 to indicate a
            // carry
            end->next->val = 99;
        }
        else // If there is no carry
        {
            // Set the value of the current node to the sum digit
            end->val = sum;
        }

        // Move the pointers along by one
        prev = end;
        end = end->next;
        elem1 = elem1->next;
        elem2 = elem2->next;
    }

    // While there are only nodes left in the first list
    while(elem1 != NULL)
    {
        int sum = elem1->val; // Store the current node's value

        if(end->val > 9)
        {
            sum++; // Add 1 if there is a carry
        }

        // Allocate memory for the next node in the answer list
        end->next = calloc(1, sizeof(struct ListNode));
        if(sum > 9) // If there is a carry
        {
            // Decrease the sum by 10, leaving just the single lower
            // digit
            end->val = sum - 10;
            // Set the value of the next node to > 9 to indicate a
            // carry
            end->next->val = 99;
        }
        else // If there is no carry
        {
            // Set the value of the current node to the sum digit
            end->val = sum;
        }

        // Move the pointers along by one
        prev = end;
        end = end->next;
        elem1 = elem1->next;
    }

    // While there are only nodes left in the second list
    while(elem2 != NULL)
    {
        int sum = elem2->val; // Store the current node's value

        if(end->val > 9)
        {
            sum++; // Add 1 if there is a carry
        }

        // Allocate memory for the next node in the answer list
        end->next = calloc(1, sizeof(struct ListNode));
        if(sum > 9) // If there is a carry
        {
            // Decrease the sum by 10, leaving just the single lower
            // digit
            end->val = sum - 10;
            // Set the value of the next node to > 9 to indicate a
            // carry
            end->next->val = 99;
        }
        else // If there is no carry
        {
            // Set the value of the current node to the sum digit
            end->val = sum;
        }

        // Move the pointers along by one
        prev = end;
        end = end->next;
        elem2 = elem2->next; 
    }

    // Remove the last node if its value is a 0
    if(end->val == 0)
    {
        prev->next = NULL;
    }
    // Set the last node's value to 1 if there is a carry
    if(end->val == 99)
    {
        end->val = 1;
    }

    // Return start which points to the first node in the answer list
    return start; 
}