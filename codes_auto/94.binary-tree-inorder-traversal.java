#
# @lc app=leetcode.cn id=94 lang=java
#
# [94] binary-tree-inorder-traversal
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
    public List<Integer> inorderTraversal(TreeNode root) {
        // 关键：巧妙运用stack入栈 中间，向左子树搜索，出栈时向右搜索
        List < Integer > res = new ArrayList < > ();
        Stack < TreeNode > stack = new Stack < > ();
        TreeNode curr = root;
        while (curr != null || !stack.isEmpty()) {
            //一直向下且向左 入栈道
            while (curr != null) {
                stack.push(curr);
                curr = curr.left;
            }
            //关键当左子树为leaf,
            //1.左子树的左子树为null左子树出栈，cur指向左子树的右子树
            //2.然后因为左子树的右子树为null, 中间出栈,指向右子树
            curr = stack.pop();
            res.add(curr.val);
            curr = curr.right;
        }
        return res;
    }
    
}
# @lc code=end