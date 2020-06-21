#
# @lc app=leetcode.cn id=1116 lang=python
#
# [1116] maximum-level-sum-of-a-binary-tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        curr_level = max_level = 1
        max_sum = float('-inf')
        queue = [root, ]
        
        while queue:
            # sum up all the nodes on the current level
            curr_sum = sum([x.val for x in queue])
            # update max_sum 
            if curr_sum > max_sum:
                max_sum, max_level = curr_sum, curr_level
            # build next level
            queue = [y for x in queue for y in [x.left, x.right] if y]
            curr_level += 1
            
        return max_level
# @lc code=end