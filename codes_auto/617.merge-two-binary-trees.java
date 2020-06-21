#
# @lc app=leetcode.cn id=617 lang=java
#
# [617] merge-two-binary-trees
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
    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
        //关键：用栈存（t1, t2), 用子树判断,t1子树非空则入栈;t1和t2都不为空则合并后存为t1，t1子树空则被t2覆盖, 

        //特判t1为空
        if(t1 == null) return t2;
        //用栈存tuple，注意tuple[0]是t1,tuple[1]是t2
        Stack < TreeNode[] > stack = new Stack < > ();
        stack.push(new TreeNode[] {t1, t2}); 
        while (!stack.isEmpty()) {
            TreeNode[] t = stack.pop();
            //入栈的（左或右）t1子树一定不为空；此时再有t2子树为空时，合并结果就是t1子树，所以不需处理
            if(t[1] == null) continue;
            //合并后存入t1
            t[0].val = t[0].val + t[1].val;
            //当t1左子树为null,合并结果为t2，存入t1
            if(t[0].left == null) t[0].left = t[1].left;
            //当t1左子树不为空，则合并t1和t2左子树 (出栈时t2左子树空则不处理，t2左子树非空则合并值)
            else stack.push(new TreeNode[] {t[0].left, t[1].left});
            //同理可得t1右子树的分类讨论
            if(t[0].right == null) t[0].right = t[1].right;
            else stack.push(new TreeNode[] {t[0].right,t[1].right});
        }
        //结果存在t1
        return t1;
    }
}
# @lc code=end