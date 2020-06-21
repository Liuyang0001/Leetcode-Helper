#
# @lc app=leetcode.cn id=518 lang=java
#
# [518] coin-change-2
#
class Solution {
    public int change(int amount, int[] coins) {
        
        int[] dp = new int[amount + 1];
        dp[0] = 1;

        for (int value : coins) { //assume we only have this kind of coin, add 1 kind at a time
            for (int j = value ; j <= amount; j++) {
                if (j - value >= 0) {
                    dp[j] += dp[j - value]; //define recurrence and bottom up
                }
            }
        }
        return dp[amount];
    }
}
# @lc code=end