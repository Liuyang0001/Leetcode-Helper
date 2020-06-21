#
# @lc app=leetcode.cn id=141 lang=java
#
# [141] linked-list-cycle
#
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
    if (head == null || head.next == null) {
        return false;
    }
    ListNode slow = head, fast = head;
    /*
        If there is a cycle, slow would finally enters and surpass the starting point (say Kth node).
        Then fast is already cycling in the loop and would take X steps to reach the ending point of the cycle (the Nth node), where X <= (N-K)/2. And slow has moved further X step during this process, it would take further X iterations for fast to catch up with slow by X steps, 1 step per iteration.
        As such, total time complexity is is O(M)+ 2*O(X) = O(K) + O(N-K) = O(N).
    */
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next; // fast moves forward to chase the end or enter a cycle
        if(slow == fast) return true;
    }
    return false;
}

}
# @lc code=end