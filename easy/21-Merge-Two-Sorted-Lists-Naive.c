/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
    if(list1 == NULL && list2 == NULL) // Both lists empty case
        return NULL;


    struct ListNode* first = list1; // Track current element of list1
    struct ListNode* second = list2; // Track current element of list2

    struct ListNode* output = malloc(sizeof(struct ListNode)); // Output list
    struct ListNode* head = output; // First output list element
    struct ListNode* prev; // Penultimate output list element

    // While there are elements left in both lists
    while(first != NULL && second != NULL)
    {
        if(first->val < second->val) // If the first list pointer's value is smaller
        {
            output->val = first->val; // Add the element to the output list
            first = first->next; // Move the first pointer to the next element
        }
        else // If the second list pointer's value is smaller
        {
            output->val = second->val; // Add the element to the output list
            second = second->next; // Move the second pointer to the next element
        }

        // Allocate memory for next output element
        output->next = malloc(sizeof(struct ListNode));
        prev = output; // Set the previous element to this element
        output = output->next; // Move the output pointer to the empty element
    }

    // While there are elements left in list1
    while(first != NULL)
    {
        output->val = first->val; // Add the element to the output list
        first = first->next; // Move the first pointer to the next element

        // Allocate memory for next output element
        output->next = malloc(sizeof(struct ListNode);
        prev = output; // Set the previous element to this element
        output = output->next; // Move the output pointer to the empty element
    }
    
    // While there are elements life in list2
    while(second != NULL)
    {
        output->val = second->val;
        second = second->next;

        // Allocate memory for the next output element
        output->next = malloc(sizeof(struct ListNode));
        prev = output; // Set the previous element to this element
        output = output->next; // Move the output pointer to the empty element
    }

    free(output); // Free empty last element
    prev->next = NULL; // Remove pointer to freed empty last element
    return head; // Return output list
}
