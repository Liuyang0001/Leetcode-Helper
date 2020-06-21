#
# @lc app=leetcode.cn id=322 lang=java
#
# [322] coin-change
#
class Solution {
   public int coinChange(int[] coins, int amount) {
       int[] f = new int[amount+1];
       f[0]=0;
       for(int i=1;i<=amount;i++){
           f[i]= Integer.MAX_VALUE;
           //find the solution for each f[i] by using deduction
           for(int value : coins){
               if(i-value>=0 && f[i-value] !=Integer.MAX_VALUE)
                    f[i] = Math.min(f[i], f[i-value]+1);
           }
       }
       return  f[amount] == Integer.MAX_VALUE? -1 : f[amount];
   }
}
# @lc code=end