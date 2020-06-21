#
# @lc app=leetcode.cn id=61 lang=cpp
#
# [61] rotate-list
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
    ListNode* rotateRight(ListNode* head, int k) {
        if(head==NULL) return head;
        ListNode* tail=head;
        
        // get size and tail
        int size=1;
        while(tail->next!=NULL){
            tail=tail->next;
            size++;
        }
        if(k%size==0) return head;
        tail->next=head; //link old_tail to old_head eg 1->2->3->4->5->NULL, 5 link to 1

        int m=size-k%size; //new head should be at mth node
        while(m-->0) tail=tail->next;
        ListNode* res=tail->next; //new head 4->
        tail->next=NULL;//new tail 3->NULL
        return res;
    }
};
# @lc code=end