#
# @lc app=leetcode.cn id=908 lang=python3
#
# [908] middle-of-the-linked-list
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast,slow = head,head
        while(fast and fast.next):
            fast=fast.next.next;
            slow=slow.next;
        return slow
# @lc code=end