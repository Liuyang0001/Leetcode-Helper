#
# @lc app=leetcode.cn id=739 lang=java
#
# [739] daily-temperatures
#
class Solution {
    public int[] dailyTemperatures(int[] T) {
        // O(N)解法，【反向】遍历构造【递减栈】: 栈里只有递减元素, 元素用T[index]代表, 
 
        //  关键1: 栈顶不满足递减时出栈 保持递减栈
        //  关键2: 由于是表示递减数的index入栈，下标差就是距离
        
        int[] ans = new int[T.length];
        Stack<Integer> decreasing = new Stack<>();

        //从后往前遍历，记录第一次升高，其实就是从后往前记录递减，发生的临界点。
        for(int i=T.length-1;i>=0;i--){
            int currentTemp = T[i];

             //关键1: 没有出现递减时，如果直接入栈的话就不是 递减栈 ，所以需要取出栈顶元素，寻找递减的临界点
            while(!decreasing.isEmpty() && currentTemp >=T[decreasing.peek()]) decreasing.pop();

            //关键2:由于是递减栈，此时栈顶元素大于当前数字，且一定是第一个大于栈顶元素的数，直接求出下标差就是二者的距离。
            ans[i] = decreasing.isEmpty()? 0: decreasing.peek() -i;

            decreasing.push(i); //此时入栈的一定是递减数，方便求距离
        }
        return ans;
    }
}
# @lc code=end