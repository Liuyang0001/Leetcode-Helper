#
# @lc app=leetcode.cn id=42 lang=java
#
# [42] trapping-rain-water
#
class Solution {
    public int trap(int[] height) {
        // 关键：i列可接的雨水是这列（左右两边最高列的较小者） 与 该列高度的 差
        int sum = 0;
        int max_left = 0;
        int max_right = 0;
        int left = 1;
        int right = height.length - 2; // 加右指针进去
        for (int i = 1; i < height.length - 1; i++) {
            //从左到右更，用left_max<right_max理解更清晰
            //【一开始】若left-1大于right+1，就一直往右移动，所经过的点只要判断maxleft与当前高度的关系
            if (height[left - 1] < height[right + 1]) {
                max_left = Math.max(max_left, height[left - 1]);
                int min = max_left;
                if (min > height[left]) {
                    sum = sum + (min - height[left]);
                }
                left++;
            //从右到左更
            } else {
                max_right = Math.max(max_right, height[right + 1]);
                int min = max_right;
                if (min > height[right]) {
                    sum = sum + (min - height[right]);
                }
                right--;
            }
        }
        return sum;

    }
}
# @lc code=end