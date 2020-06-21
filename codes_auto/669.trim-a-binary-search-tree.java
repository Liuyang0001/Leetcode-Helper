#
# @lc app=leetcode.cn id=669 lang=java
#
# [669] trim-a-binary-search-tree
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
    public TreeNode trimBST(TreeNode root, int L, int R) {
        // 关键：当 node.val > R，那么右子树也一定超出范围，修剪后该节点直接被trmBST(左子树)替代
        // 类似的，小于下限的节点被trmBST(右子树)直接替代。
        if(root == null) return root;
        else if(root.val < L) return trimBST(root.right, L, R);
        else if(root.val > R) return trimBST(root.left, L, R);
        // 没出现替代, 就继续递归子树
        root.left = trimBST(root.left, L, R);
        root.right = trimBST(root.right, L, R);
        return root;
    }
}
# @lc code=end