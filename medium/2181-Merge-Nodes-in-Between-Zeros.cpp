/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeNodes(ListNode* head) {
        ListNode* start = head; // Stores the start of the current segment
        ListNode* end; // Stores the end of the current segment
        
        while(start != NULL) // While there are segments left
        {
            end = start->next; // Set end to the first non-zero value
            
            int sum = 0; // Stores sum of the values of the segment
            while(end->val != 0) // For each non-zero value in the segment
            {
                sum += end->val; // Add the value to the sum
                end = end->next; // Go to the next element
            }
            start->val = sum; // Set the starting 0 node's value to the sum
            
            // Set the next value in the list to the next 0 node if there
            // is another segment, or NULL if there are no segments left
            start->next = end->next != NULL ? end : NULL;
            start = start->next; // Move to the next 0 node(or NULL if the end)
        }
        
        return head;
    }
};
