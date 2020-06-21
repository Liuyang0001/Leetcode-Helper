#
# @lc app=leetcode.cn id=21 lang=cpp
#
# [21] merge-two-sorted-lists
#
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode(0);//use a dummy head to record the head of the merged list
        ListNode* cur = dummy;
        while(l1 && l2){
            if(l1->val <= l2->val){
                cur->next = l1;
                l1 = l1->next;
            }else{
                cur->next = l2;
                l2 = l2->next;
            }
           cur = cur->next;
        }// break when one list reaches the end
        if(l1) cur->next = l1; // add the remaining nodes in the non-ending list.
        if(l2) cur->next = l2;
        return dummy->next;
    }
};
# @lc code=end