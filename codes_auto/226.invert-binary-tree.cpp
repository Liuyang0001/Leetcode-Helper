#
# @lc app=leetcode.cn id=226 lang=cpp
#
# [226] invert-binary-tree
#
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
    typedef struct TreeNode* ptr;
struct TreeNode* invertTree(struct TreeNode* root){
    if(!root || (!root->left && !root->right))
        return root;
    ptr r = invertTree(root->right);
    ptr l = invertTree(root->left);
    root->left = r;
    root->right = l;
    return root;
}
};
# @lc code=end