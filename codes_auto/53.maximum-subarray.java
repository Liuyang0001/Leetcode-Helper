#
# @lc app=leetcode.cn id=53 lang=java
#
# [53] maximum-subarray
#
class Solution {
    public int maxSubArray(int[] nums) {
        //dp[i] = Math.max(dp[i- 1] + nums[i], nums[i]);	
        int ans = nums[0];
        int sum = 0;
        for(int num: nums) {
            //compare if sum + nums[i] > nums[i]
            if(sum > 0) {
                sum += num; 
            } else {
                sum = num;
            }
            ans = Math.max(ans, sum);
        }
        return ans;
    }
}
# @lc code=end