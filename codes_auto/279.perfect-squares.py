#
# @lc app=leetcode.cn id=279 lang=python
#
# [279] perfect-squares
#
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        from collections import deque
        if n == 0: return 0
        queue = deque([n]) # doubly linked
        step = 0
        visited = set()
        while(queue):
            step+=1 # complete 1 layer
            l=len(queue)
            for _ in range(l): # examine every node in this layer for ans using BFS
                tmp=queue.pop() # last out
                for i in range(1,int(tmp**0.5)+1):
                    x=tmp-i**2
                    if(x==0): # answer
                        return step
                    if(x not in visited):
                        queue.appendleft(x) #IMPORTANT to ensure elements in 1 layer are out in order
                        visited.add(x)
        return step
# @lc code=end