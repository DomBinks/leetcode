/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* getTargetCopy(TreeNode* original, TreeNode* cloned, TreeNode* target) {
        TreeNode* ret; // Stores returned node from recursive call
        if(original == target) // If the target node has been found
        {
            return cloned; // Return the corresponding cloned node
        }
        else // If the target node hasn't been found
        {
            if(original->left) // If there is a left child node
            {
                // Search the left side of the tree
                ret = getTargetCopy(original->left, cloned->left, target);
                if(ret) // If the target node is found
                    return ret; // Return the corresponding cloned node
            }
            if(cloned->right) // If there is a right child node
            {
                // Search the right side of the tree
                ret = getTargetCopy(original->right, cloned->right, target);
                if(ret) // If the target node is found
                    return ret; // Return the corresponding cloned node
            }
        }
        
        return NULL; // Return NULL if the target isn't found
    }
};
