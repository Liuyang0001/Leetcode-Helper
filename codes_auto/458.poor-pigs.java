#
# @lc app=leetcode.cn id=458 lang=java
#
# [458] poor-pigs
#
class Solution {
    public int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
        //一只小猪最多能够验证5桶水
        //两只验证25桶水，第1只猪喝每一行所有编号的水桶的混合水，第2只猪喝每一列所有编号的水桶的混合水
        //如果有三只猪， 可以用类似的方法构建5x5x5的立方阵，最多可测125桶水
        //关键：那么 x 只猪的信息量等价于一个 【x 位的 p/m+1 进制数】
        int states = (int)(minutesToTest/minutesToDie) + 1;
        return (int) Math.ceil(Math.log(buckets) / Math.log(states));
    }
}
# @lc code=end