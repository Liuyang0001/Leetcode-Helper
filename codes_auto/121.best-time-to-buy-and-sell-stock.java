#
# @lc app=leetcode.cn id=121 lang=java
#
# [121] best-time-to-buy-and-sell-stock
#
class Solution {
    public int maxProfit(int[] prices) {
        int minPrice = Integer.MAX_VALUE;
        int maxProfit = 0;
        for(int i =0;i<prices.length;i++){
            if(minPrice > prices[i]){
                minPrice = prices[i];
            }else if(maxProfit < prices[i]-minPrice){
                maxProfit = prices[i]-minPrice;
            }
            //System.out.printf("%d %d\n",minPrice,maxProfit);
        }
        return maxProfit;
    }
}
# @lc code=end