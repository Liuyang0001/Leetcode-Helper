#
# @lc app=leetcode.cn id=20 lang=python
#
# [20] valid-parentheses
#
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {')':'(','}':'{',']':'['}
        stack = []
        for c in s:
            if c in mapping:
                top = stack.pop() if stack else '#'
                if top != mapping[c]:
                    return False
            else:
                stack.append(c)
        return not stack
# @lc code=end