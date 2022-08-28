#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>

struct ListNode {
     int val;
     struct ListNode *next;
 };

// Returns the length of the list with first element head
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

    printf("%d\n", isPalindrome(&a));

    return 0;
}