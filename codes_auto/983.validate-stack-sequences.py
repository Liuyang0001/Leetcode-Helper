#
# @lc app=leetcode.cn id=983 lang=python3
#
# [983] validate-stack-sequences
#
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i,j,k,n = 0,0,0,len(pushed)
        # i : pushed array 当前未被检查的element位置
        # j : popped array 当前未被检查的element位置
        # k : 当前正在比对是否相当的位置，表示top of stack in pushed array, to be poped out if equal.

        while i<n:
            pushed[k] = pushed[i] #不断向前检查pushed array,类似于一个inplace stack的入栈
            while j<n and k >= 0 and pushed[k] == popped[j]:#比较当前的top of the pushed与top of poped
                k-=1 #top出栈，于是需要比对的top of pushed回移一位
                j+=1 #poped出栈，于是比对的top of poped进一位
            k+=1
            i+=1
        return j==n
# @lc code=end