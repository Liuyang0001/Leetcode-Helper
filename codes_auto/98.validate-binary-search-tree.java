#
# @lc app=leetcode.cn id=98 lang=java
#
# [98] validate-binary-search-tree
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
    // 关键： 记录upper limit和lower limit，满足左中右的顺序。
    // 每个node的值是它的左子树的上限，它的下限 也是它的左子树的下限，必是他作为右子树的parent
    // 每个node的值是它的右子树的下限，他的上限 也是它的右子树的上限，必是他作为左子树的parent


  public boolean valid(Integer lower, TreeNode node,Integer upper) {
    if (node == null) return true;

    int val = node.val;
    if (lower != null && val <= lower) return false; 
    if (upper != null && val >= upper) return false; 

    if (! valid(val, node.right, upper)) return false; //node的值是它的右子树的下限
    if (! valid(lower, node.left, val)) return false;  //node的值是它的左子树的上限
    return true;
  }

  public boolean isValidBST(TreeNode root) {
    return valid(null, root, null);
  }
}
# @lc code=end