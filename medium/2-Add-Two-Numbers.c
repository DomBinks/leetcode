#include <stdlib.h>
#include <stdio.h>

int max(int a, int b)
{
    return a > b ? a : b;

}
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

struct ListNode* sumTwoNumbers(struct ListNode* l1, struct ListNode* l2, struct ListNode* carry)
{
    struct ListNode* a;
    struct ListNode* b;
    int sum = l1->val + l2->val;

    if(carry != NULL && carry->val > 9)
    {
        sum++;
        printf("Used carry");

        struct ListNode* temp = carry;
        carry = carry->next;
        free(carry);
    }
    printf("l1: %d, l2:%d\n", l1->val, l2->val);
    printf("sum %d\n", sum);

    if(sum > 9)
    {
        a = calloc(1, sizeof(struct ListNode));
        b = calloc(1, sizeof(struct ListNode));

        a->val = 999;
        a->next = b;
        b->val = sum - 10;
        b->next = carry;
        printf("a:%d b:%d\n", a->val, b->val);
    }
    else
    {
        a = calloc(1, sizeof(struct ListNode));
        a->val = sum;
        a->next = carry;
        printf("a:%d\n", a->val);
    }

    return a;
}


struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){

    int length1 = listLength(l1);
    int length2 = listLength(l2);
    struct ListNode* end = NULL;

    while(length1 > 0 && length2 > 0)
    {
        struct ListNode* elem1 = l1;
        struct ListNode* elem2 = l2;        

        for(int i = 1; i < max(length1, length2); i++)
        {
            if(length1 < i)
            {
                elem1 = elem1->next;
            }
            if(length2 < i)
            {
                elem2 = elem2->next;
            }
        }
        printf("values: a: %d b: %d\n", elem1->val, elem2->val);

        end = sumTwoNumbers(elem1, elem2, end);

        length1--;
        length2--;
    }

    while(length1 > 0)
    {
        struct ListNode* elem1 = l1;

        for(int i = 1; i < length1; i++)
        {
            elem1 = elem1->next;
        }

        if(elem1->next != NULL && (elem1->next)->val > 9)
        {
            elem1->val++; 
            struct ListNode* temp = elem1->next;
            elem1->next = (elem1->next)->next; 
            free(temp);
        }

        length1--;
    }
    while(length2 > 0)
    {
        struct ListNode* elem2 = l2;

        for(int i = 1; i < length2; i++)
        {
            elem2 = elem2->next;
        }

        if(elem2->next != NULL && (elem2->next)->val > 9)
        {
            elem2->val++; 
            struct ListNode* temp = elem2->next;
            elem2->next = (elem2->next)->next; 
            free(temp);
        }

        length2--;
    }

    return end;
}

int main(int argc, char **argv)
{
    struct ListNode* a1 = calloc(1, sizeof(struct ListNode));
    struct ListNode* a2 = calloc(1, sizeof(struct ListNode));
    struct ListNode* a3 = calloc(1, sizeof(struct ListNode));
    struct ListNode* b1 = calloc(1, sizeof(struct ListNode));
    struct ListNode* b2 = calloc(1, sizeof(struct ListNode));

    a1->val = 1;
    a1->next = a2;
    a2->val = 2;
    a2->next = a3;
    a3->val = 6;
    a3->next = NULL;
    b1->val = 4;
    b1->next = b2;
    b2->val = 5;
    b2->next = NULL;

    struct ListNode* ans = addTwoNumbers(a1, b1);

    printf("\nAnswer:\n");
    while(ans != NULL)
    {
        printf("%d\n", ans->val);
        ans = ans->next;
    }
    return 0;
}