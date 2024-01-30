/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

// Recursive function that returns the amount of palindromicPaths
int getPalindromicPaths(struct TreeNode* root, int *occurrences)
{
    int out = 0; // Number of palindromic paths

    // Toggle the occurrences array value for the current node value
    if(occurrences[root->val] == 1)
        occurrences[root->val] = 0;
    else
        occurrences[root->val] = 1;

    // Recursive case - end of a path hasn't been reached
    if(root->left != NULL || root->right != NULL)
    {
        if(root->left != NULL) // If there is a left child node
        {
            int occurrencesLeft[10]; // Create a copy of the occurrences array
            memcpy(occurrencesLeft, occurrences, 10*sizeof(int));

            // Look at the path towards the left child node
            out += getPalindromicPaths(root->left, occurrencesLeft);
        }
        if(root->right != NULL)
        {
            int occurrencesRight[10]; // Create a copy of the occurrences array
            memcpy(occurrencesRight, occurrences, 10*sizeof(int));

            // Look at the path towards the right child node
            out += getPalindromicPaths(root->right, occurrencesRight);
        }
    }
    // Base case - end of a path has been reached
    else
    {
        // Sum all the values in the occurrences array
        int sum = 0;
        for(int i = 1; i < 10; i++)
        {
            sum += occurrences[i];
        }

        // If at most 1 value has an odd number of occurrences in this path
        if(sum <= 1)
            out++; // Increment out as this path is palindromic
    }
    
    return out; // Return the number of palindromic paths
}

// Returns the number of pseudo-palindromic paths from the root node to leaf nodes
int pseudoPalindromicPaths (struct TreeNode* root)
{
    // Occurrence arrays track whether the path has an even or odd number of
    // nodes with a given value.
    // 0 = Even number of nodes, 1 = Odd number of nodes
    // If the sum of the values is > 1 then there are multiple values that have
    // an odd number of nodes, which means the path isn't pseudo-palindromic

    int palindromicPaths = 0; // Number of palindromic paths

    if(root->left != NULL || root->right != NULL) // If there are paths 
    {
        if(root->left != NULL) // If are paths to the left
        {
            // Create an array to store occurrences
            int occurrencesLeft[10] = {0};
            occurrencesLeft[root->val] = 1;

            // Add the number of palindromic paths to the total
            palindromicPaths += getPalindromicPaths(root->left, occurrencesLeft);
        }
        if(root->right != NULL)
        {
            // Create an array to store occurrences
            int occurrencesRight[10] = {0};
            occurrencesRight[root->val] = 1;

            // Add the number of palindromic paths to the total
            palindromicPaths += getPalindromicPaths(root->right, occurrencesRight);
        }
    }
    else // If there is no path
    {
        if(root != NULL) // If there is just 1 node
            palindromicPaths++; // Counts as a palindromic path so increment
    }
    
    return palindromicPaths;
}
