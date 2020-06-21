#
# @lc app=leetcode.cn id=144 lang=java
#
# [144] binary-tree-preorder-traversal
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
 import java.util.List;
 import java.util.ArrayList;

class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        // 利用stack先压入右，再压入左 
        // 按照 Top->Bottom 和 Left->Right，符合前序遍历的顺序。
        List<Integer> result = new ArrayList<>();
        if (root == null) {
		return result;
	}
	Stack<TreeNode> stack = new Stack<>();
	stack.push(root);
	while (!stack.isEmpty()) {
        //关键：巧妙运用Stack FIFO的特性不断 延伸左子树
		TreeNode node = stack.pop();
		result.add(node.val);
        //先压入右，再压入左，这样一直压出的也是左，形成pre-order
		if (node.right != null) {
			stack.push(node.right);
		}
		if (node.left != null) {
			stack.push(node.left);
		}
	}
    return result;
    }
}
# @lc code=end