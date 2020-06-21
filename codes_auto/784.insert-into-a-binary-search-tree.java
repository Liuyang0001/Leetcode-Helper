#
# @lc app=leetcode.cn id=784 lang=java
#
# [784] insert-into-a-binary-search-tree
#
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode insertIntoBST(TreeNode root, int val) {
        //Note：递归最易懂。但空间复杂度O(lgN)。
        //关键：【迭代】至insert的位置，空间复杂度降至O(1)
        if(root == null) return new TreeNode(val);
        TreeNode  current = root;
        while (true){
            // insert into the right subtree
            if (val > current.val){
                if(current.right == null) {
                    current.right = new TreeNode(val);
                    return root;
                }else{
                    current = current.right;
                }
            } 
            //insert into the left subtree
            else {
                if(current.left == null) {
                    current.left = new TreeNode(val);
                    return root;
                }else{
                    current = current.left;
                }
            }
        } 
    }
}
# @lc code=end