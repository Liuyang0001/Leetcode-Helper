#
# @lc app=leetcode.cn id=109 lang=java
#
# [109] convert-sorted-list-to-binary-search-tree
#
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
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

    private ListNode head;
    //find size of the list
   public int findSize(ListNode head){
        ListNode ptr = head;
        int c = 0;
        while (ptr != null){
            ptr = ptr.next;
            c++;
        }
        return c;
   }
    public TreeNode sortedListToBST(ListNode head){
        // Get the size of the linked list first
        this.head = head;
        int size = this.findSize(head);
        //关键1: 包括size
        return convert(0,size);
    }

    public TreeNode convert(int l, int r){
        //Recursively form a BST out of linked list from l --> r
            // 关键2: 包括等于的情况
            if(l >= r) return null;

            int mid = (l + r) / 2;

            // First step of simulated inorder traversal. Recursively form the left half
            TreeNode left = this.convert(l, mid);

            //Once left half is traversed, process the current node
            TreeNode node = new TreeNode(head.val);  
            node.left = left;

            // 关键3: 遵循InOrder的顺序，在left half跑完之后，马上移到下一步，保证node一直是mid
            head = head.next;

            // Recurse on the right hand side and form BST out of them
            node.right = this.convert(mid + 1, r);
            return node;
    }


}
# @lc code=end