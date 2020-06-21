#
# @lc app=leetcode.cn id=143 lang=cpp
#
# [143] reorder-list
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
    void reorderList(ListNode* head) {
        ListNode* current = head;
        stack<ListNode*> s;
        //use p != NULL to push every node into a stack
         while(current) {
            s.push(current);
            current = current->next;
        }
        //1->2->3->4->5, we have middle node as 3, then 2->4, 4->3, etc
        if(s.size() <= 2) return; // IMPORTANT to avoid operation on NULL pointer
        current = head; // use p to iterate
        int size = s.size(); // IMPORTANT as size of the stack is changing dynamically
        for(int i = 0; i < size / 2; i++) {
            ListNode* nextNode = current->next;
            current->next = s.top();
            s.pop();
            current->next->next = nextNode;
            current = nextNode;
        }
        current->next = NULL; // IMPORTANT to put tail for "middle node"
        return;
    }
};
# @lc code=end