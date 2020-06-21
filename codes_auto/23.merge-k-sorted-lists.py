#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] merge-k-sorted-lists
#
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

       #【注意】heapq里比较的机制是从元组首位0开始，即遇到相同，就比较元组下一位，
       # 这题刚好node值有重复的，ListNode无法被比较，因此存入 node.val，node_list_index
        que , curs = [] , [] # curs存K个链表滑动的头指针
        for index, node in enumerate(lists):
                if node!=None:
                    heapq.heappush(que ,(node.val, index))
                curs.append(node)

        dummy_node = ListNode(-1)
        cur = dummy_node
        while que:
            val, index =  heapq.heappop(que)
            cur.next = lists[index]
            cur = cur.next
            lists[index] = lists[index].next # 记得指向下一个
            if lists[index] != None:
                heapq.heappush(que, (lists[index].val, index))
        return dummy_node.next
# @lc code=end