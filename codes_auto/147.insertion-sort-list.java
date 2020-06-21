#
# @lc app=leetcode.cn id=147 lang=java
#
# [147] insertion-sort-list
#
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode insertionSortList(ListNode head) {
        ListNode dummy = new ListNode(-1);
        ListNode toInsert = dummy;
        ListNode cur = head;//Insert from head

        while (cur != null) {
            // temp is used to store the next node to insert, as cur.next is changed after insertion
            ListNode tmp = cur.next; 
            // find the position to insert after
            while (toInsert.next != null && toInsert.next.val < cur.val) toInsert = toInsert.next;
            cur.next = toInsert.next;
            toInsert.next = cur;
            toInsert = dummy;//revert the toInsert position to dummy (can be optimized using a tail)
            cur = tmp;
        }
        return dummy.next;
    }
}
# @lc code=end