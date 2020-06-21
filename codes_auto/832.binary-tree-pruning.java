#
# @lc app=leetcode.cn id=832 lang=java
#
# [832] binary-tree-pruning
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
    //关键：用recursion helper 寻找subtree的和
    public boolean hasOneRecursion (TreeNode root){
        if(root == null) return false;
        boolean leftHasOne = hasOneRecursion(root.left);
        boolean rightHasOne = hasOneRecursion(root.right);
        if(!leftHasOne) root.left = null;
        if(!rightHasOne) root.right = null;
        return root.val == 1 ||leftHasOne ||rightHasOne;
    }

    public TreeNode pruneTree(TreeNode root) {
        return hasOneRecursion(root) ? root : null; //特判root及子树都是0的情况
    }
}
# @lc code=end