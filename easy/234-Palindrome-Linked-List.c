#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>

struct ListNode {
     int val;
     struct ListNode *next;
 };

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
 
bool isPalindrome(struct ListNode* head)
{
    int length = listLength(head);
    int midpoint = length / 2;

    int *firstHalf = calloc(midpoint, sizeof(int));
    struct ListNode* current = head;
    for(int i = 0; i < midpoint; i++)
    {
        firstHalf[i] = current->val;
        current = current->next;
    }

    if(length % 2 != 0)
    {
        current = current->next;
    }

    for(int i = 0; i < midpoint; i++)
    {
        printf("%d %d\n", current->val, firstHalf[midpoint - i - 1]);
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

int main(int argc, char *argv)
{
    struct ListNode a = {0};
    a.val = 1;
    struct ListNode b = {0};
    b.val = 2;
    struct ListNode c = {0};
    c.val = 3;
    struct ListNode d = {0};
    d.val = 4;
    a.next = &b;
    b.next = &c;
    c.next = &d;

    if(isPalindrome(&a) == true)
    {
        printf("True\n");
    }
    else
    {
        printf("False\n");
    }

    return 0;
}