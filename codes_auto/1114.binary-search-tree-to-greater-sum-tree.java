#
# @lc app=leetcode.cn id=1114 lang=java
#
# [1114] binary-search-tree-to-greater-sum-tree
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
    //关键：中序遍历左根右，倒序即为右、根、左
    int lastVal = 0;
    public TreeNode bstToGst(TreeNode root) {
        if(root == null) return root;
        // 1.遍历右子树
        if(root.right != null) bstToGst(root.right);

        // 2.访问当前节点. 加上前一个节点更新后的值，更新最后一次访问的节点值
        root.val += lastVal;
        lastVal = root.val;

        // 3.遍历左子树
         if(root.left != null) bstToGst(root.left);

        return root;

    }
}
# @lc code=end