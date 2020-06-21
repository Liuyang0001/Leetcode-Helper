#
# @lc app=leetcode.cn id=91 lang=java
#
# [91] decode-ways
#
class Solution {
    public int numDecodings(String s) {
         /*
        Let dp[i] be the number of decode ways for str s[0...i].

        1. s[i] is 0: s[i-1] must be 1 or 2, then dp[i] = dp[i-2]; otherwise 0;
       
        2. s[i-1] is 1 or s[i-1]is 2 and 1<= s[i] <=6: 
        then dp[i]= dp[i-1] + dp[i-2]  //split or combine the last 2 to encode
        
        otherwise: s[i-1] >= 3 or s[i-1]is 2 and s[i] > 6: 
        dp[i] = dp[i-1]       //NO update in # of ways as split is the only possible way
        */
        if(s.startsWith("0")) return 0;
        char[] ss = s.toCharArray();
        int pre = 1, curr = 1;//dp[-1] = dp[0] = 1
        for (int i = 1; i < ss.length; i++) {
            int tmp = curr;
            if (ss[i] == '0')
                if (ss[i - 1] == '1' || ss[i - 1] == '2') curr = pre;
                else return 0;
            else if (ss[i - 1] == '1' || (ss[i - 1] == '2' && ss[i] >= '1' && ss[i] <= '6'))
                curr = curr + pre;
            pre = tmp;
        }
        return curr;
    
}

}
# @lc code=end