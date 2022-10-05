/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int rangeSumBST(TreeNode* root, int low, int high) {
        int out = 0;
        
        // If the current node value is in the range
        if(root->val >= low && root->val <= high)
            out += root->val; // Add the value to the total
        // If there is a left child node
        if(root->left != NULL)
            // Check the left child node 
            out += rangeSumBST(root->left, low, high);
        // If there is a right child now
        if(root->right != NULL)
            // Check the right child node
            out += rangeSumBST(root->right, low, high);
        
        return out;
    }
};
