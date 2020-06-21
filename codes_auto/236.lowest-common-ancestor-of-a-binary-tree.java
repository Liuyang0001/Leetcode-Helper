#
# @lc app=leetcode.cn id=236 lang=java
#
# [236] lowest-common-ancestor-of-a-binary-tree
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
    TreeNode ans = null;

    public boolean recursionToFindIfHasPorQ(TreeNode current, TreeNode p, TreeNode q){
            // If reached the end of a branch, return false.
            if(current == null) return false;

            // Left Recursion
            int left = recursionToFindIfHasPorQ(current.left, p, q)? 1 : 0;

            // Right Recursion
            int right = recursionToFindIfHasPorQ(current.right, p, q)? 1 : 0;

            // If the current node is one of p or q
            int mid = (current == p || current == q)? 1 : 0;

            // If any two of the three flags left, right or mid become True.
            if(left+right+mid >= 2) this.ans = current;

            // Return True if either of the three bool values is True.
            return left+right+mid > 0;
    }

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
         // Traversed the tree
         recursionToFindIfHasPorQ(root, p ,q);
         return ans;
    }
}
# @lc code=end