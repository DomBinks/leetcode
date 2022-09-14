/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int recur(struct TreeNode* root, int *occurrences)
{
    int out = 0;

    if(occurrences[root->val] == 1)
        occurrences[root->val] = 0;
    else
        occurrences[root->val] = 1;

    if(root->left != NULL)
    {
        int occurrencesLeft[9];
        memcpy(occurrencesLeft, occurrences, 9*sizeof(int));
        out += recur(root->left, occurrencesLeft);
    }
    else
    {
        int sum = 0;
        for(int i = 0; i < 9; i++)
        {
            sum += occurrences[i];
        }

        if(sum <= 1)
            out++;
    }

    if(root->right != NULL)
    {
        int occurrencesRight[9];
        memcpy(occurrencesRight, occurrences, 9*sizeof(int));
        out += recur(root->right, occurrencesRight);
    }
    else
    {
        int sum = 0;
        for(int i = 0; i < 9; i++)
        {
            sum += occurrences[i];
        }

        if(sum <= 1)
            out++;
    }

    return out;
}

int pseudoPalindromicPaths (struct TreeNode* root)
{
    int palindromicPaths = 0;

    int occurancesLeft[9] = {0};
    occurancesLeft[root->val] = 1;
    palindromicPaths += recur(root->left, occurancesLeft);

    int occurancesRight[9] = {0};
    occurancesRight[root->val] = 1;
    palindromicPaths += recur(root->right, occurancesRight);

    
    return palindromicPaths;
}
